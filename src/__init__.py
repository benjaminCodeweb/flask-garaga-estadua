from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy 
from .config import Config 

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()

def crear_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autos.db'

    db.init_app(app=app)
    
    from .routes import auto_bp
    
    app.register_blueprint(blueprint= auto_bp)
    return app 




