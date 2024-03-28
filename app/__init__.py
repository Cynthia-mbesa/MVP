from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    login_manager.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
