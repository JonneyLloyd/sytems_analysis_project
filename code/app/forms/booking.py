from flask import flash
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from app.api.booking_view import BookingView

class BookingForm(Form):
    user_id = StringField('User ID', [Required()])

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

    def validate(self):
        valid = super(BookingForm, self).validate()
        if not valid:
            return False
        user_id = self.user_id.data
        if not BookingView.get_booking_for_user(user_id):
            flash('User not found', 'danger')  # TODO: enum
            return False
        else:
            return True
