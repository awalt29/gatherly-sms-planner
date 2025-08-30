# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies including PostgreSQL development headers
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 8000 (Railway should map this automatically)
EXPOSE 8000

# Run the ultra-minimal Python server with hardcoded port
CMD python3 -c "
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            response = {'message': 'SUCCESS! Railway deployment working!', 'status': 'healthy'}
        elif self.path == '/health':
            response = {'status': 'healthy', 'message': 'Health check passed'}
        else:
            response = {'error': 'Not found', 'path': self.path}
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

print('Starting server on port 8000...')
HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
"
