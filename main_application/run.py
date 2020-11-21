import http.server
import socketserver

import requests

from app.settings.settings import Settings

PORT = Settings().GRPC_PORT

x = requests.get(f"http://localhost:{PORT}")

print (x)
