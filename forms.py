from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, email_validator


# Create a class module
class RegistrationForm(FlaskForm):
    # Make the username field
    username = StringField('Username',
                           # ▶︎   Create also validators, and the length of username
                           validators=[DataRequired(), Length(min=2, max=20)])
    # Make the email field
    email = StringField('Email',
                        # ▶︎   Insert data and what kind of data
                        validators=[DataRequired(), Email()])
    # Make the password field
    password = PasswordField('Password',
                             # ▶︎   Create also validators, and the length of password
                             validators=[DataRequired(), Length(min=4, max=12)])
    # Make the confirm password field
    confirm_password = PasswordField('Confirm Password',
                                     # ▶︎   Create also validators, has to be equal to password ↰
                                     validators=[DataRequired(), EqualTo('password')])
    # Submit btn
    submit = SubmitField('Sign Up')


# Create a class module
class LoginForm(FlaskForm):
    # Make the username field
    username = StringField('Username',
                           # ▶︎   Create also validators, and the length of username
                           validators=[DataRequired(), Length(min=2, max=20)])
    # # Make the email field
    email = StringField('Email',
                        # ▶︎   Insert data and what kind of data
                        validators=[DataRequired(), Email()])
    # Make the password field
    password = PasswordField('Password',
                             # ▶︎   Create also validators, and the length of password
                             validators=[DataRequired(), Length(min=4, max=12)])
    # Make a remember field
    remember = BooleanField('Remember Me')
    # Login btn
    submit = SubmitField('Login')
