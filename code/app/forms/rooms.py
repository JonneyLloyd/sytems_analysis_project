from flask import flash
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import Required, EqualTo
from app.api.room_manager import RoomManager

class RoomAvailabilityForm(Form):
    date = StringField('Date', [Required()])
    room_type = StringField('Room Type', [Required()])
    def __init__(self, *args, **kwargs):
        super(RoomAvailabilityForm, self).__init__(*args, **kwargs)
    def validate(self):
        valid = super(RoomAvailabilityForm, self).validate()
        if not valid:
            return False
        date = self.date.data
        room_type = self.room_type.data
        if not RoomManager.get_rooms_occupied_on_date(date, room_type):
            flash('Error', 'danger')  # TODO: enum
            return False
        else:
            return True
