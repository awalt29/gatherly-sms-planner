#!/usr/bin/env python3
"""
Minimal test WSGI for Railway deployment debugging
"""
import os

print("🚀 Starting minimal Flask app...")
print(f"PORT environment variable: {os.environ.get('PORT', 'NOT SET')}")

try:
    from flask import Flask
    print("✅ Flask imported successfully")
    
    app = Flask(__name__)
    print("✅ Flask app created")
    
    @app.route('/')
    def hello():
        return {'message': 'Hello from Railway!', 'status': 'working'}, 200
    
    @app.route('/health')
    def health():
        return {'status': 'healthy', 'message': 'Minimal app is running'}, 200
    
    @app.route('/test')
    def test():
        env_vars = {k: v for k, v in os.environ.items() if not k.startswith('_')}
        return {'message': 'Test endpoint working', 'environment': env_vars}, 200
    
    print("✅ Routes defined")
    print("🎯 Minimal app ready for Railway")
    
except Exception as e:
    print(f"❌ Error creating minimal app: {e}")
    import traceback
    traceback.print_exc()
    raise

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
