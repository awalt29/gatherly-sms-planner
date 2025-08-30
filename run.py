#!/usr/bin/env python3
"""
Production entry point for the SMS Event Planner application.
Used by Railway and other deployment platforms.
"""
import os
from app import create_app

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    # For Railway deployment, use PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    
    # Run the application
    app.run(host='0.0.0.0', port=port, debug=False)
