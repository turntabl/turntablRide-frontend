import json
import requests
import threading
from werkzeug import Request, Response
from werkzeug.serving import make_server
from kivy.clock import Clock
from queue import Empty, Queue
import global_var as glob

queue = Queue()


def oauth_server(goauth_client, client_secret):
    @Request.application
    def callback(request):
        code = request.args.get("code")
        if code:
            token_endpoint = goauth_client.oauth_endpoints["token_endpoint"]
            token_url, headers, body = goauth_client.web_client.prepare_token_request(
                token_endpoint,
                authorization_response=request.url,
                redirect_url="https://127.0.0.1:9004/",
                code=code,
            )

            token_response = requests.post(
                token_url,
                headers=headers,
                data=body,
                auth=(
                    goauth_client.client_id,
                    client_secret,
                ),
            )

            goauth_client.web_client.parse_request_body_response(
                json.dumps(token_response.json())
            )

            queue.put(goauth_client.web_client.token["id_token"])
            glob.stop_thread = True
            Clock.schedule_once(
                lambda *args: goauth_client.succ_listener(
                    goauth_client.web_client.token["id_token"]
                ),
                0,
            )
            return Response("Return to the application to proceed", 200)
        return Response("Invalid Parameters.", 401)

    return make_server("localhost", 9004, callback, ssl_context="adhoc")


def run_server(server):
    t = threading.Thread(target=server.serve_forever)
    t.start()
    token = check_for_stop()
    print("shutdown from run_server function")
    server.shutdown()
    t.join()
    return token


def check_for_stop():
    if glob.stop_thread:
        try:
            return queue.get_nowait()
        except Empty:
            return None
    try:
        glob.stop_thread = True
        return queue.get(timeout=100)
    except Empty:
        check_for_stop()
