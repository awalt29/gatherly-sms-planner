# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install gunicorn (Railway seems to expect it)
RUN pip install gunicorn

# Create a simple Flask app that Railway can run with gunicorn
RUN echo 'from flask import Flask\napp = Flask(__name__)\n\n@app.route("/")\ndef home():\n    return {"message": "SUCCESS! Railway working with Flask!", "status": "healthy"}\n\n@app.route("/health")\ndef health():\n    return {"status": "healthy", "message": "Health check OK"}\n\nif __name__ == "__main__":\n    app.run(host="0.0.0.0", port=8000)' > app.py

# Expose port 8000
EXPOSE 8000

# Let Railway use gunicorn (it seems to override CMD anyway)
CMD gunicorn app:app --bind 0.0.0.0:8000 --workers 1
