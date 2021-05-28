from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from application.models import User

class SignUpForm(FlaskForm):
    first_Name = StringField('First Name', validators=[DataRequired()])
    last_Name = StringField('Last Name', validators=[DataRequired()])
    # user_Name = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_Password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    accept_ToU = BooleanField('I accept the Terms of Use & Privacy Policy')
    submit = SubmitField('Sign Up')

    # def validate_fields(self, field):
    #     if True:
    #         raise ValidationError('Validation Message')
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email Already Exist!! Try another Email.')





class LoginForm(FlaskForm):
    # user_Name = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
