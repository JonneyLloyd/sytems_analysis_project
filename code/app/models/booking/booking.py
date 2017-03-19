from app import app, db


class Booking(db.Model):
    '''
    Database representation of bookings
    '''
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    _user_id = db.Column(db.Integer, nullable=False)
    _room_id = db.Column(db.Integer, nullable=False)
    _start_date = db.Column(db.Date, nullable=False)
    _end_date = db.Column(db.Date, nullable=False)
    _credit_card = db.Column(db.Integer, nullable=False)
    _booking_price = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, room_id, start_date, end_date, credit_card, booking_price):
        self._user_id = user_id
        self._room_id = room_id
        self._start_date = start_date
	self._end_date = end_date
	self._credit_card = credit_card
	self._booking_price = booking_price

    @property
    def user_id(self):
        return self._user_id

    @property
    def room_id(self):
        return self._room_id

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def credit_card(self):
        return self._credit_card

    @property
    def booking_price(self):
        return self._booking_price


    @user_id.setter
    def set_user_id(self, user_id):
        self._user_id = user_id
 
    @room_id.setter
    def set_room_id(self, room_id):
        self._room_id = room_id

    @start_date.setter
    def set_start_date(self, start_date):
        self._start_date = start_date

    @end_date.setter
    def set_end_date(self, end_date):
        self._end_date = end_date

    @credit_card.setter
    def set_credit_card(self, credit_card):
        self._credit_card = credit_card

    @booking_price.setter
    def set_booking_price(self, booking_price):
        self._booking_price = booking_price



    def __repr__(self):
        return '<Booking ref %r>' % self.id
