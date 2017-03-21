from flask import current_app as app
from app.extensions import db
from sqlalchemy.ext.hybrid import hybrid_property


class Room(db.Model):
    '''
    Database representation of a room
    '''
    __tablename__ = 'rooms'

    _id = db.Column('id', db.Integer, primary_key=True)
    _type = db.Column('type', db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    _number = db.Column('number', db.Integer, nullable=False)
    _occupancy = db.Column('occupancy', db.Integer, nullable=False)
    _availability = db.Column('availability', db.String(120), nullable=False)
    _clean = db.Column('clean', db.Boolean, nullable=False)

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

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def occupancy(self):
        return self._occupancy

    @occupancy.setter
    def occupancy(self, value):
        self._occupancy = value

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, value):
        self._availability = value

    @property
    def clean(self):
        return self._clean

    @clean.setter
    def clean(self, value):
        self._clean = value

    def __repr__(self):
        return '<Room %r:%r:%r>' % self._id, self._type, self._number
