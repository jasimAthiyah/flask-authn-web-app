from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
import hashlib
from flask_login import login_user, login_required, logout_user, current_user

# blue print means a blueprint of our application that 
# has bunch of urls inside
auth = Blueprint('auth',__name__)
salt = "5gz"

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        database_password = password + salt
        hashed_input_password = hashlib.sha256(database_password.encode()).hexdigest()
        
        # Filter all of the users that have the email in email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            if hashed_input_password == user.password:
                flash('Logged in successfully!', category='success')
                # stores flash session, remembers that the user is logged in unless 
                # the user clears browsing history
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')
        
    
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',  methods=['GET','POST'] )
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        
        #checking if the user alrdy exists if they try to sign up again
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email should be greater that 4 characters',category='error')
        elif len(firstName) <2:
            flash('First Name should be greater than 1 character',category='error')
        elif len(password1) < 7:
            flash('Your password is too short.',category='error')
        elif password1 != password2:
            flash("Your passwords don\'t match",category='error')
        else:
            database_password = password1+salt
            hashed = hashlib.sha256(database_password.encode()).hexdigest()
            # User is user defined from models.py
            new_user = User(email=email, firstName=firstName, password=hashed)
            db.session.add(new_user)
            db.session.commit()
            #flash message for account creation
            flash('Account created successfully', category='success')
            
             # Fetch the newly added user from the database
            user = User.query.filter_by(email=email).first()
            
            # Log in the user
            login_user(user, remember=True)
           
            
        
    return render_template("sign_up.html")