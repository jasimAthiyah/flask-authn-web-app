from flask import Blueprint
# blue print means a blueprint of our application that 
# has bunch of urls inside

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logging out</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign up</p>"