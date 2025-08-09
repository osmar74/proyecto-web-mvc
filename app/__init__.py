# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='views', static_folder='../static')

    # Importar y registrar el blueprint principal
    from .controllers.main import main_bp
    app.register_blueprint(main_bp)

    return app

