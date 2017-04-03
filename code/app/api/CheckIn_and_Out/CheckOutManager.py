from flask import request,render_template
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm as Form
from app.extensions import db
from app.models.booking import Booking
from app.models.room import Room
class CheckOutManager(object):
    @staticmethod
    def Judge(creditnum):
        room_db = db.session.query(Room).filter(Booking.credit_card == creditnum, Booking.room_id == Room.id)
        if room_db.first() is None:
            return False
        else:
            for m in room_db.all():
                m.clean = 1;
                m.availability = 'Y';
            db.session.commit();
            return True;