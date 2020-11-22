import http.server
import socketserver
from time import sleep

import requests

from app.settings.settings import Settings

PORT = Settings().GRPC_PORT

while True:
    print(requests.get(f"http://localhost:{PORT}"))
    sleep(5)
