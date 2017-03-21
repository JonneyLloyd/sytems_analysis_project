from flask import flash
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from app.auth.login import LoginManager


class RegisterForm(Form):
    email = StringField('Email', [Required(), Email()])  # TODO stricter validation
    password = PasswordField('Password', [Required()])
    password_confirmation = PasswordField(
        'Confirm Password',
        [Required(), EqualTo('password', message='Passwords must be equal')]
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def validate(self):
        valid = super(RegisterForm, self).validate()
        if not valid:
            return False
        email = self.email.data
        password = self.password.data
        if not LoginManager.register(email, password):
            flash('This email is already in use.', 'danger')  # TODO: enum
            return False
        else:
            return True


class LoginForm(Form):
    email = StringField('email', [Required(), Email()])
    password = PasswordField('password', [Required()])

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    def validate(self):
        valid = super(LoginForm, self).validate()
        if not valid:
            return False
        email = self.email.data
        password = self.password.data
        if not LoginManager.login(email, password):
            flash('Incorrect email or password. Please try again.', 'danger')  # TODO: enum
            return False
        else:
            return True
