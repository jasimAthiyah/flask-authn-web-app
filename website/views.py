from flask import Blueprint
# blue print means a blueprint of our application that 
# has bunch of urls inside

# what is __name__?
#is a special variable that represents the name of the current module. 
# so when views is imported the __name__ changes to views (the file name)
views = Blueprint('views',__name__)

# decorator in python for defining routes
@views.route('/')
# this is a route function, so when / is in the url, it displays content inside home function
def home():
    return "<h1>Test</h1>"