from app.models.user import User
from app.models.booking import Booking
from datetime import datetime

class BookingView(object):

    @staticmethod
    def get_booking_for_user(user_id):
    	booking = Booking.query.filter_by(user_id=user_id).first()
    	result = {'room_id': booking.room_id, 'start_date': booking.start_date,
    		 'end_date': booking.end_date, 'booking_price': booking.booking_price,
             'name':booking.user.details.first_name}
    	if not booking:
    		return False
    	else:
    		return result

    @staticmethod
    def get_booking_by_credit_card(credit_card):
    	booking = Booking.query.filter_by(credit_card=credit_card).first()
    	result = {'room_id': booking.room_id, 'start_date': booking.start_date,
    		 'end_date': booking.end_date, 'booking_price': booking.booking_price}
    	if not booking:
    		return False
    	else:
    		return result

    @staticmethod
    def get_booking_on_date(date):
        result = []
        bookings = Booking.query.filter(Booking.start_date <= datetime.strptime(date, '%Y-%m-%d').date(),
                                        Booking.end_date >= datetime.strptime(date, '%Y-%m-%d').date()).all()
        if not bookings:
    		return False
        for booking in bookings:
            info = {
                'room_id': booking.room_id,
                'start_date': booking.start_date,
                'end_date': booking.end_date,
                'booking_price': booking.booking_price,
                'email':booking.user.email
            }
            result.append(info)
    	return result
