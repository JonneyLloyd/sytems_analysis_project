from app import app, db


class Booking(db.Model):
    '''
    Database representation of bookings
    '''
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    room_id = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    credit_card = db.Column(db.Integer, nullable=False)
    booking_price = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, room_id, start_date, end_date, credit_card, booking_price):
        self.user_id = user_id
        self.room_id = room_id
        self.start_date = start_date
	self.end_date = end_date
	self.credit_card = credit_card
	self.booking_price = booking_price

    def set_user_id(self, user_id):
        self.user_id = user_id
 
    def set_room_id(self, room_id):
        self.room_id = room_id

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_credit_card(self, credit_card):
        self.credit_card = credit_card

    def set_booking_price(self, booking_price):
        self.booking_price = booking_price



    def __repr__(self):
        return '<Booking ref %r>' % self.id
