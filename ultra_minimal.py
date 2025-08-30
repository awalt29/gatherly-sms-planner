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
                'port_env': os.environ.get('PORT', 'NOT_SET'),
                'all_env': {k: v for k, v in os.environ.items() if 'PORT' in k.upper()}
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
    # More robust port detection
    port_env = os.environ.get('PORT', '8000')
    print(f"PORT environment variable: '{port_env}'")
    
    # Handle case where PORT might be '$PORT' literal string
    if port_env == '$PORT' or not port_env.isdigit():
        print(f"Invalid PORT value '{port_env}', using default 8000")
        port = 8000
    else:
        port = int(port_env)
    
    print(f"Starting ultra-minimal server on port {port}")
    print(f"All environment variables with 'PORT': {[(k, v) for k, v in os.environ.items() if 'PORT' in k.upper()]}")
    
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()
