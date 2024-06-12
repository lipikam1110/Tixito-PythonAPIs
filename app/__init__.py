from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
# from flask import Flask
from flask_cors import CORS



db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # app = Flask(__name__)
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/Authentication')  # Adjusted URL prefix

    return app
