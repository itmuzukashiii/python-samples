#!/usr/bin/env python3

import http.server
import socketserver

PORT = 54321
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()

