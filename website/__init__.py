## this file makes the website folder a python package
from flask import Flask

# creates a flask app
def create_app():
    app = Flask(__name__)
    # below code encrypts/ secure cookies n session data
    app.config['SECRET_KEY'] = "web-a--auth-flask"
    
    from .views import views
    from .auth import auth
    
    #This makes the routes defined in the blueprint accessible within the main application.
    app.register_blueprint(views,url_prefix = '/')
    app.register_blueprint(auth,url_prefix = '/')
    
    return app