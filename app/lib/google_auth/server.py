import json
import threading
import requests
from werkzeug import Request, Response
from werkzeug.serving import make_server
from queue import Queue
import app.lib.google_auth.globals as glob

token_queue = Queue()


def get_oauth_server(goauth_client, client_secret: str):
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
            token_url, headers, body = goauth_client.web_client.prepare_token_request(
                glob.google_endpoints["TOKEN_ENDPOINT"],
                authorization_response=request.url.replace("http", "https"),
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
            token_queue.put(goauth_client.web_client.token["id_token"])
            goauth_client.succ_listener(goauth_client.web_client.token)
            return Response("Return to the application to proceed", 200)
        return Response("Invalid Parameters.", 401)

    return make_server(glob.HOST, glob.PORT, callback)


def wait_for_token():
    return token_queue.get()


def trigger_server_stop():
    token_queue.put(None)


def serve_server(server):
    threading.Thread(target=server.handle_request, daemon=True).start()
