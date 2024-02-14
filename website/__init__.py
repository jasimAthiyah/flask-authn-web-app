## this file makes the website folder a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

# creates a flask app
def create_app():
    app = Flask(__name__)
    # below code encrypts/ secure cookies n session data
    app.config['SECRET_KEY'] = "web-app-auth-flask"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flask_auth_web_app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking, it's not needed for MySQL
    db.init_app(app)
    
    
    from .views import views
    from .auth import auth
    
    #This makes the routes defined in the blueprint accessible within the main application.
    app.register_blueprint(views,url_prefix = '/')
    app.register_blueprint(auth,url_prefix = '/')
    
    from .models import User,Note    
     
    with app.app_context():
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    # telling flask how we load a user, what user we're looking for with the id
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('created database')