from .main import main
from .page import page
from .routes_registers import category

def init_app(app):
    app.register_blueprint(main)
    app.register_blueprint(page)
    app.register_blueprint(category)
