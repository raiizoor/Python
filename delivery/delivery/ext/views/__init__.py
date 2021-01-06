from .main import main
from .page import page

def init_app(app):
    app.register_blueprint(main)
    app.register_blueprint(page)
