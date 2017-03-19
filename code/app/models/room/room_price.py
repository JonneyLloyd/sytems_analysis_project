from app import app, db


class Room_Price(db.Model):
    '''
    Database representation of room prices
    '''
    __tablename__ = 'room_price'

    _id = db.Column(db.Integer, primary_key=True)
    _type = db.Column(db.String(120), nullable=False)
    _price_weekday = db.Column(db.Float, nullable=False)
    _price_weekend = db.Column(db.Float, nullable=False)

    def __init__(self, type, price_weekday, price_weekend):
        self._type = type
        self._price_weekday = price_weekday
        self._price_weekend = price_weekend

    @property
    def type(self):
        return self._type

    @property
    def price_weekday(self):
        return self._price_weekday

    @property
    def price_weekend(self):
        return self._price_weekend
 
    @type.setter
    def set_type(self, type):
        self._type = type

    @price_weekday.setter
    def set_price_weekday(self, price_weekday):
        self._price_weekday = price_weekday

    @price_weekday.setter
    def set_price_weekend(self, price_weekend):
        self._price_weekend = price_weekend



    def __repr__(self):
        return '<Room %r>' % self.type
