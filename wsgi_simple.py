#!/usr/bin/env python3
"""
WSGI entry point for production deployment
"""
import os
import sys

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

print(f"WSGI starting from directory: {current_dir}")

try:
    from app import create_app
    print("✅ Successfully imported create_app")
    
    # Create the Flask application
    app = create_app()
    print("✅ Flask app created successfully")
    
    # Simple database initialization - non-blocking
    try:
        from app import db
        with app.app_context():
            db.create_all()
        print("✅ Database tables initialized")
    except Exception as db_error:
        print(f"⚠️  Database initialization warning: {db_error}")
        # Continue anyway - app can still run
    
except Exception as e:
    print(f"❌ Critical error during app initialization: {e}")
    import traceback
    traceback.print_exc()
    raise

if __name__ == '__main__':
    # For direct execution (not used with Gunicorn)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
