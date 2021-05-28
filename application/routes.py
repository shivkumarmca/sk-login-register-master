from flask_bcrypt import generate_password_hash
from flask_login.utils import logout_user
from application import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from application.forms import LoginForm, SignUpForm
from application.models import User
from flask_login import login_user, current_user


# app.config['SECRET_KEY'] = "shiv"

@app.route("/")
@app.route("/index")
def home():
    return render_template('home.html', title='Home')

@app.route("/login", methods=['GET','POST'])
def login():
    if(current_user.is_authenticated):
        return redirect(url_for('home'))
    form = LoginForm()    
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:        
            flash(f'Login Failure!', 'danger')
            # return render_template('sign-in-blue-bg.html', title='Login', form=form)
    return render_template('sign-in-blue-bg.html', title='Login', form=form)


@app.route("/register", methods=['GET','POST'])
def register():
    if(current_user.is_authenticated):
        return redirect(url_for('home'))
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data).decode('UTF-8')
        user = User(first_Name = form.first_Name.data, last_Name = form.last_Name.data, email = form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Account Created!, Please Login.', 'success')
        return redirect(url_for('login'))
    return render_template('sign-up-blue-bg.html', title='Sign Up', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

