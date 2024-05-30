#!/usr/bin/python3

'''The http.server module of the Python standard library provides
 base classes for implementing web servers'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    '''Class that inherits from BaseHTTPRequestHandler
    to handle HTTP requests.'''


def do_GET(self):
    '''
    Handles GET requests to our API.
    Returns a simple text response for the root endpoint,
    a JSON response for the /data endpoint, and a 404 error
    for any other undefined endpoint.
    '''
    if self.path == '/':
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, this is a simple API!')
    elif self.path == '/data':
        data = {"name": "John", "age": 30, "city": "New York"}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    elif self.path == '/status':
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')
    else:
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Endpoint not found')


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    '''
    Starts a simple HTTP server with the given port number.

    Args:
    server_class: The HTTP server class to use (default HTTPServer).
    handler_class: The HTTP request handler class to use (default MyServer).
    port: The port number to use (default 8000).
    '''
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
