from app.models.booking import Booking
from flask import g, session, request
from app.extensions import db
from app.models.booking import Booking
from app.models.room import Room
from app.models.room import RoomPrice
from datetime import datetime, date , timedelta
import datetime
import time

class changePrice(object):

    @staticmethod
    def pricechange(user_id,room_id,weekday_price,weekend_price):
        room_update = (RoomPrice.query.filter_by(_id=room_id).first())
        room_update._price_weekday = weekday_price
        room_update._price_weekend = weekend_price

        db.session.add(room_update)
        db.session.commit()


