from flask import flash
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, ValidationError, HiddenField, SelectField
from wtforms.validators import Required, Email, EqualTo, Length
from app.models.role import RoleEnum, RoleFactory


class ProfileForm(Form):
    user_id = HiddenField()
    first_name = StringField('First name', [Required()])
    last_name = StringField('Last name', [Required()])
    contact_number = StringField('Contact number', [Length(min=8, max=30, message='Invalid phone number')])  # TODO stricter validation


class RegisterForm(Form):
    email = StringField('Email', [Required(), Email()])  # TODO stricter validation
    password = PasswordField('Password', [Required()])
    password_confirmation = PasswordField(
        'Confirm Password',
        [Required(), EqualTo('password', message='Passwords must be equal')]
    )


class LoginForm(Form):
    email = StringField('email', [Required(), Email()])
    password = PasswordField('password', [Required()])

class RegisterFormStaff(Form):
    email = StringField('Email', [Required(), Email()])  # TODO stricter validation
    choices = [('3','Guest'), ('0','Admin'),('1','Manger'),('2','Staff')]
    role = SelectField("Role: ",coerce=str, choices=choices)
    # role =StringField('Role', [Required()])  # TODO stricter validation
    password = PasswordField('Password', [Required()])
    password_confirmation = PasswordField(
        'Confirm Password',
        [Required(), EqualTo('password', message='Passwords must be equal')]
    )

class DeleteFormStaff(Form):
    email = StringField('Email', [Required(), Email()])  # TODO stricter validation
