# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Create a simple test server
RUN echo 'from http.server import HTTPServer, BaseHTTPRequestHandler\nimport json\n\nclass Handler(BaseHTTPRequestHandler):\n    def do_GET(self):\n        if self.path == "/":\n            response = {"message": "SUCCESS! Railway working!", "status": "healthy"}\n        elif self.path == "/health":\n            response = {"status": "healthy", "message": "Health check OK"}\n        else:\n            response = {"error": "Not found"}\n        self.send_response(200)\n        self.send_header("Content-Type", "application/json")\n        self.end_headers()\n        self.wfile.write(json.dumps(response).encode())\n\nprint("Starting server on port 8000...")\nHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()' > test_server.py

# Expose port 8000
EXPOSE 8000

# Run the test server
CMD python test_server.py
