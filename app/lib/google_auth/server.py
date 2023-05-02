import json
import requests
from werkzeug import Request, Response
from werkzeug.serving import make_server
from app.lib.google_auth.globals import HOST, PORT, CALLBACK_URL, google_endpoints


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
                google_endpoints["TOKEN_ENDPOINT"],
                authorization_response=request.url.replace("http", "https"),
                redirect_url=CALLBACK_URL,
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
            return Response("Return to the application to proceed", 200)
        return Response("Invalid Parameters.", 401)

    return make_server(HOST, PORT, callback)
