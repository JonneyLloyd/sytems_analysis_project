from app import app, db


class Room(db.Model):
    '''
    Database representation of a room
    '''
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    _type = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    _number = db.Column(db.Integer, nullable=False)
    _occupancy = db.Column(db.Integer, nullable=False)
    _availability = db.Column(db.String(120), nullable=False)
    _clean = db.Column(db.Boolean, nullable=False) 

    ''' 
	TODO
	use backref  to room_price
	and another backref in booking to room
    '''

    def __init__(self, type, number, occupancy, availability, clean):
        self._type = type
        self._number = number
        self._occupancy = occupancy
	self._availability = availability
	self._clean = clean

    @property
    def type(self):
        return self._type

    @property
    def number(self):
        return self._number

    @property
    def occupancy(self):
        return self._occupancy

    @property
    def availability(self):
        return self._availability

    @property
    def clean(self):
        return self._clean

    @availability.setter
    def set_availability(self, availability):
        self._availability = availability

    @clean.setter
    def set_clean(self, clean):
        self._clean = clean

    @occupancy.setter
    def set_occupancy(self, occupancy):
        self._occupancy = occupancy

    @number.setter
    def set_number(self, number):
        self._number = number

    @type.setter
    def set_type(self, type):
        self._type = type


    def __repr__(self):
        return '<Room %r>' % self.number
