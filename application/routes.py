from flask_wtf import form
from application import app
from flask import render_template, url_for, flash, redirect
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
        if form.email.data == 'shivkumargwl@gmail.com' and form.password.data == 'shiv':
            # print(form.email.data)
            flash(f'Logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Failure!', 'danger')
            # return render_template('sign-in-blue-bg.html', title='Login', form=form)
    return render_template('sign-in-blue-bg.html', title='Login', form=form)


@app.route("/register", methods=['GET','POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.email.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('sign-up-blue-bg.html', title='Sign Up', form=form)