from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "SUCCESS! Railway working with Flask!", "status": "healthy"}

@app.route("/health")
def health():
    return {"status": "healthy", "message": "Health check OK"}

@app.route("/webhook", methods=['POST'])
def webhook():
    return {"message": "Webhook endpoint ready", "status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
