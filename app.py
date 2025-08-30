from flask import Flask
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def home():
    logger.info("Home route accessed")
    return {"message": "SUCCESS! Railway working with Flask!", "status": "healthy"}

@app.route("/health")
def health():
    logger.info("Health check accessed")
    return {"status": "healthy", "message": "Health check OK"}

@app.route("/webhook", methods=['POST'])
def webhook():
    logger.info("Webhook accessed")
    return {"message": "Webhook endpoint ready", "status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"Starting Flask app on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
