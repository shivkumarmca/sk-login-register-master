from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_Name = db.Column(db.String(120), unique=True, nullable = False )
    last_Name = db.Column(db.String(120), unique=True, nullable = False )
    email = db.Column(db.String(200), unique=True, nullable = False )
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.first_Name} + ' ', '{self.last_Name}','{self.email}','{self.password}')"

    