#!/usr/bin/env python3
"""
Ultra-minimal test - just Python with no dependencies
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            response = {
                'message': 'Ultra-minimal Python server working!',
                'status': 'success',
                'port': os.environ.get('PORT', 'NOT_SET')
            }
        elif self.path == '/health':
            response = {
                'status': 'healthy',
                'message': 'Simple HTTP server running'
            }
        else:
            response = {
                'error': 'Not found',
                'path': self.path
            }
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print(f"Starting ultra-minimal server on port {port}")
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()
