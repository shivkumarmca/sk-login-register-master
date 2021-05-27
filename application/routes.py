from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/login")
def login():
    return render_template('sign-in-blue-bg.html')


@app.route("/register")
def register():
    return render_template('sign-up-blue-bg.html')