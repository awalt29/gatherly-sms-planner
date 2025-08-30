# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a simple Flask app
COPY . .

# Create app.py if it doesn't exist
RUN echo 'from flask import Flask\napp = Flask(__name__)\n\n@app.route("/")\ndef home():\n    return {"message": "SUCCESS! Railway working with Flask!", "status": "healthy"}\n\n@app.route("/health")\ndef health():\n    return {"status": "healthy", "message": "Health check OK"}\n\nif __name__ == "__main__":\n    import os\n    port = int(os.environ.get("PORT", 8000))\n    app.run(host="0.0.0.0", port=port)' > app.py

# Expose port
EXPOSE $PORT

# Use gunicorn as Railway expects
CMD gunicorn app:app --bind 0.0.0.0:$PORT
