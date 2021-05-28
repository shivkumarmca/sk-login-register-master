from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

# add DB Functions
db = SQLAlchemy(app)

# hased password genration and decryption
bcrypt = Bcrypt(app)

# to handle sessions related to login
login_manager = LoginManager(app)

# db.init_app(app)
from application import routes