import json
import requests
import threading
from werkzeug import Request, Response
from werkzeug.serving import make_server
from queue import Empty, Queue
import app.google_auth.globals as glob

queue = Queue()


def oauth_server(goauth_client, client_secret):
    """
    Defines a server with a simple handler.

    Parameters
    ----------
    goauth_client : GoogleOAuth object
        An object of the GoogleOAuth class
    client_secret : str
        The client secret of the application provided by google.

    Return
    ------
    A BaseWSGIServer
    """

    @Request.application
    def callback(request):
        code = request.args.get("code")
        if code:
            token_endpoint = goauth_client.oauth_endpoints["TOKEN_ENDPOINT"]
            token_url, headers, body = goauth_client.web_client.prepare_token_request(
                token_endpoint,
                authorization_response=request.url,
                redirect_url=glob.CALLBACK_URL,
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
            goauth_client.succ_listener(goauth_client.web_client.token["id_token"])
            return Response("Return to the application to proceed", 200)
        return Response("Invalid Parameters.", 401)

    return make_server("localhost", 9004, callback, ssl_context="adhoc")


def run_server(server):
    """
    Runs the server and shutdowns upon receiving a value in
    the queue or when triggered.

    Parameters
    ----------
    server : BaseWSGIServer
        A BaseWSGIServer instance

    Return
    ------
    token : Any
        A value put into the queue by the server.
    """
    t = threading.Thread(target=server.serve_forever)
    t.start()
    glob.stop_thread = False
    token = check_for_stop()
    print("shutdown from run_server function")
    server.shutdown()
    t.join()
    return token


def check_for_stop():
    """
    Checks for the stop_thread and returns if set else continues to
    wait for value to be put in queue.
    If value is put in queue, then it returns.

    Return
    ------
    token : Any
        Can be a any value or None.
        None if no value is in queue and stop_thread is set to true.
    """
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
