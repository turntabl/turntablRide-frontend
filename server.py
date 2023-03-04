import json
import os
from flask import Flask, request
import requests
from config import get_google_config, client_google

server = Flask("Authentication Server")


def start_server():
    server.run(port=9004, ssl_context='adhoc')


def stop_server():
    pass

@server.route("/loginGoogle/callbackGoogle")
def callback():
    code = request.args.get("code")
    token_endpoint = get_google_config()["token_endpoint"]
    # print("this is it", request.url)

    token_url, headers, body = client_google.prepare_token_request(token_endpoint,authorization_response=request.url,redirect_url="https://127.0.0.1:9004/loginGoogle/callbackGoogle",code=code)

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(os.getenv("GOOGLE_CLIENT_ID"), os.getenv("GOOGLE_CLIENT_SECRET")),
    )

    client_google.parse_request_body_response(json.dumps(token_response.json()))
    print(client_google.access_token)
    return "<h2>Return back to application to proceed</h2>"