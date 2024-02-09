from flask import Blueprint, render_template
# blue print means a blueprint of our application that 
# has bunch of urls inside

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    # the text part is a variable/argument we are passing that can be accessed in login.html
    return render_template("login.html", text="testing", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logging out</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")