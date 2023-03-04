import os
from flask import Flask, request
import requests

server = Flask("Authentication Server")


def start_server():
    server.run(port=9004)


def stop_server():
    pass

@server.route("/loginGoogle/callbackGoogle")
def callback():
    code = request.args.get("code")
    from google_oauth import client_google, google_provider_cfg
    token_endpoint = google_provider_cfg["token_endpoint"]
    print(client_google.client_id)
    token_url, headers, body = client_google.prepare_token_request(
    token_endpoint,
    authorization_response=request.url,
    redirect_url="http://127.0.0.1:9004/loginGoogle/callbackGoogle",
    code=code,)

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(os.getenv("GOOGLE_CLIENT_ID"), os.getenv("GOOGLE_CLIENT_SECRET")),
    )

    print(token_response)
    return "<h2>Return back to application to proceed</h2>"