from app.models.user import User
from app.models.booking import Booking


class Booking_view(object):

    @staticmethod
    def get_booking_for_user(user_id):
	booking = Booking.query.filter_by(user_id=user_id).first()
	result = {'room_id': booking.room_id, 'start_date': booking.start_date,
		 'end_date': booking.end_date, 'booking_price': booking.booking_price}
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

