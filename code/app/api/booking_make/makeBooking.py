from app.models.booking import Booking
from flask import g, session, request
from app.extensions import db
from app.models.booking import Booking
from app.models.room import Room
from app.models.room import RoomPrice
from datetime import datetime, date , timedelta
import datetime
import time

class makeBooking(object):

    @staticmethod
    def bookingmake(user_id,room_id,start_date,end_date,credit_card):
        new_start = start_date.replace('-',"")
        new_end = end_date.replace('-',"")
        date1 = datetime.datetime.strptime(new_start, '%Y%m%d').date()
        date2 =datetime.datetime.strptime(new_end, '%Y%m%d').date()

        distance =  date2 -date1
        distance = distance.days

        total_price =0

        # Get total price of room
        room_wanted = (RoomPrice.query.filter_by(_id=room_id).first())
        weekday_price = room_wanted._price_weekday
        weekend_price = room_wanted._price_weekend
        for i in range(0,distance):
            day_booked=(date1 + timedelta(days=i))
            # gets day as an integer 0 being monday and 6 being sunday
            start_day = day_booked.weekday()
            print(start_day)
            # is it a weekday?
            if ( start_day < 5):
                total_price += weekday_price
            # if not, is weekend
            else:
                total_price += weekend_price


        room_booking = Booking(user_id,room_id,start_date,end_date,credit_card,total_price)
        db.session.add(room_booking)
        db.session.commit()

