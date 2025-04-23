from flask import Flask
from flask_login import LoginManager
from app.auth.user import User
from flask_sqlalchemy import SQLAlchemy 
from app.models import db, DBUser

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    app.secret_key = app.config.get('SECRET_KEY')

    db.init_app(app)
    login_manager.init_app(app)

    from .auth.routes import auth_bp
    from .routes import core_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(core_bp)

    return app 


@login_manager.user_loader
def load_user(user_id):
    return DBUser.query.get(int(user_id))