from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
import logging
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    """Application factory"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV') or 'default'
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Configure logging
    if not app.debug and not app.testing:
        logging.basicConfig(level=logging.INFO)
    
    # Register blueprints
    from app.routes.sms import sms_bp
    from app.routes.dashboard import dashboard_bp
    app.register_blueprint(sms_bp, url_prefix='/sms')
    app.register_blueprint(dashboard_bp)
    
    # Add simple root endpoint
    @app.route('/')
    def root():
        return {'message': 'Gatherly SMS Event Planner', 'version': '2.0', 'status': 'running'}, 200
    
    # Add health check endpoint
    @app.route('/health')
    def health_check():
        try:
            # Test database connection
            with app.app_context():
                result = db.session.execute(db.text('SELECT 1'))
                db.session.commit()
            return {'status': 'healthy', 'message': 'Gatherly is running', 'database': 'connected'}, 200
        except Exception as e:
            return {'status': 'unhealthy', 'message': f'Database error: {str(e)}'}, 503
    
    # Add simple status endpoint that doesn't require database
    @app.route('/status')
    def status_check():
        import os
        return {
            'status': 'running',
            'message': 'Gatherly app is running',
            'env_vars': {
                'DATABASE_URL': 'SET' if os.environ.get('DATABASE_URL') else 'MISSING',
                'TWILIO_ACCOUNT_SID': 'SET' if os.environ.get('TWILIO_ACCOUNT_SID') else 'MISSING',
                'PORT': os.environ.get('PORT', 'Not set')
            }
        }, 200
    
    @app.route('/api')
    def api_info():
        return {'message': 'Gatherly API', 'version': '2.0', 'status': 'active'}, 200
    
    # Import models to ensure they're registered with SQLAlchemy
    with app.app_context():
        from app.models import planner, event, guest, guest_state, contact, availability
    
    return app
