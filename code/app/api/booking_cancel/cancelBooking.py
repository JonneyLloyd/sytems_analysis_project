
from app.extensions import db
from app.models.booking import Booking


class cancelBooking(object):

    @staticmethod
    def bookingcancel(credit_card):
        exists = Booking.query.filter_by(credit_card=credit_card).scalar() is not None
        if(exists):
            Booking.query.filter_by(credit_card=credit_card).delete()
            db.session.commit()
            return True
        else:
            return False

