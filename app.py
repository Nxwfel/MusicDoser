from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

from dotenv import load_dotenv
import os

# Initialize extensions
db = SQLAlchemy()  # ORM
migrate = Migrate()
login_manager = LoginManager() 
bcrypt = Bcrypt() 
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    load_dotenv()

    # Load configuration from environment variables
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['RECAPTCHA_PUBLIC_KEY'] = os.getenv('RECAPTCHA_PUBLIC_KEY')
    app.config['RECAPTCHA_PRIVATE_KEY'] = os.getenv('RECAPTCHA_PRIVATE_KEY')


    # Initialize extensions with the Flask app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    bcrypt.init_app(app)

    # Set up the login view
    login_manager.login_view = 'login'  # Redirect to the login page if not logged in

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import routes
    from routes import register_routes
    register_routes(app, db, bcrypt)

    return app
