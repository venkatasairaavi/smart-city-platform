from flask import Flask
from .auth.routes import auth_bp
from .routes import core_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')


    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(core_bp)

    return app 