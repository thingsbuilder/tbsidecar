import http.server
import socketserver

from app.settings.settings import Settings

PORT = Settings().GRPC_PORT
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
