import json
import os
from flask import Flask
import requests
from config import get_google_config, client_google
from multiprocessing import Process
import threading
from queue import Queue

from werkzeug import Request, Response
from werkzeug.serving import make_server


def oauth_server(queue):
    @Request.application
    def callback(request):
        code = request.args.get("code")
        token_endpoint = get_google_config()["token_endpoint"]
        # print("this is it", request.url)

        token_url, headers, body = client_google.prepare_token_request(token_endpoint,authorization_response=request.url,redirect_url="https://127.0.0.1:9004/",code=code)

        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(os.getenv("GOOGLE_CLIENT_ID"), os.getenv("GOOGLE_CLIENT_SECRET")),
        )

        client_google.parse_request_body_response(json.dumps(token_response.json()))
        queue.put(client_google.access_token)
        return Response("<h2>Return to the application to proceed</h2>", 200)
    
    return make_server("localhost", 9004, callback, ssl_context='adhoc')


    # server.run(port=9004, ssl_context='adhoc')
def run_server(server, queue):
    t = threading.Thread(target=server.serve_forever)
    t.start()
    token = queue.get(block=True)
    server.shutdown()
    t.join()
    return token


server_process = Process(target=oauth_server)
def start_oauth_server():
    server_process.start()


def stop_server(server):
    if server_process.is_alive():
        server_process.terminate()
        server_process.join()
    
    
