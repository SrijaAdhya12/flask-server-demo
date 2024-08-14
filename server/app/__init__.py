from flask import Flask
from app.routes.home import home_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    return app
