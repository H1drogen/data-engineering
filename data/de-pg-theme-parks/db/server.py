import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from connection import db
import re

PORT = 8888
socket = ('', PORT)

class Handler(BaseHTTPRequestHandler):
    def create_response(self, response):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

    def do_GET(self):
        if self.path == '/healthcheck':
            response = json.dumps({
              "message": "everything okay"
            })
            self.create_response(response)

        if self.path == '/parks':
            response = json.dumps(
                db.run('SELECT * FROM parks')
            )
            self.create_response(response)

        
        if match := re.search(r"\/ride\/(\d+)", self.path):
            ride_id = match.group(1)
            response = json.dumps(
                db.run('SELECT * FROM rides WHERE ride_id = :ride_id', ride_id=ride_id)
            )
            self.create_response(response)

    def do_POST(self):
        if self.path.split('/')[0][1] == ['parks', 'rides']:
       



with HTTPServer(socket, Handler) as server:
    print(f'serving at port {PORT}')
    server.serve_forever()


