# Python http.server that sets Access-Control-Allow-Origin header.
# https://gist.github.com/razor-x/9542707

import http.server
from http.server import HTTPServer

PORT = 8000


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)


httpd = HTTPServer(("127.0.0.1", 8000), HTTPRequestHandler)
print("Hosting server on port 8000")
httpd.serve_forever()
