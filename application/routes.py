from flask_wtf import form
from werkzeug.utils import redirect
from application import app
from flask import render_template, url_for, flash
from application.forms import LoginForm, SignUpForm


app.config['SECRET_KEY'] = "shiv"

@app.route("/")
@app.route("/index")
def home():    
    return render_template('home.html', title='Home')

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'(form.email.data) logged in!', 'success')
        return redirect(url_for('home'))
    return render_template('sign-in-blue-bg.html', title='Login', form=form)


@app.route("/register", methods=['GET','POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'Account Created for (form.email.data)!', 'success')
        return redirect(url_for('login'))
    
    return render_template('sign-up-blue-bg.html', title='Sign Up', form=form)