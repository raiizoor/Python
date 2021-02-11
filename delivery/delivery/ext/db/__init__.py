from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = "danger"
login_manager.login_message = (
    "Você precisa logar antes de tentar acessar essa página!"
)

def init_app(app):
    db.init_app(app)
    login_manager.init_app(app)
