#!/usr/bin/python3

'''The http.server module of the Python standard library provides
 base classes for implementing web servers'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    '''A simple HTTP server that handles GET requests and serves JSON data.'''

    def do_GET(self):

        '''Respond to a GET request by serving JSON data for specific endpoints
        or a simple text greeting. Undefined endpoints return a 404 error.'''

        # Define the header for content-type as JSON
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Check the endpoint and provide the appropriate response
        if self.path == '/':
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            # Serve the JSON data
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            # Serve the status endpoint
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode())
        else:
            # Handle undefined endpoints
            self.send_error(404, "Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler,
        port=8000):
    '''Run the HTTP server on a specified port.'''
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
