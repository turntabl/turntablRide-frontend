import json
import requests
import threading
from werkzeug import Request, Response
from werkzeug.serving import make_server
from kivy.clock import Clock
from queue import Queue


queue = Queue()


def oauth_server(goauth_client, after_login, client_id, client_secret):
    @Request.application
    def callback(request):
        code = request.args.get("code")
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
                client_id,
                client_secret,
            ),
        )

        goauth_client.web_client.parse_request_body_response(
            json.dumps(token_response.json())
        )

        queue.put(goauth_client.web_client.access_token)
        Clock.schedule_once(lambda *args: after_login("", "", ""), 0)
        return Response("Return to the application to proceed", 200)

    return make_server("localhost", 9004, callback, ssl_context="adhoc")


def run_server(server):
    t = threading.Thread(target=server.serve_forever)
    t.start()
    print("server started")
    token = queue.get(block=True)
    server.shutdown()
    t.join()
    return token
