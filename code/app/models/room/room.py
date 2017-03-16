from app import app, db


class Room(db.Model):
    '''
    Database representation of a room
    '''
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    occupancy = db.Column(db.Integer, nullable=False)
    availability = db.Column(db.String(120), nullable=False)
    clean = db.Column(db.Boolean, nullable=False) 

    ''' 
	TODO
	use backref  to room_price
	and another backref in booking to room
    '''

    def __init__(self, type, number, occupancy, availability, clean):
        self.type = type
        self.number = number
        self.occupancy = occupancy
	self.availability = availability
	self.clean = clean

    def set_availability(self, availability):
        self.availability = availability
 
    def set_clean(self, clean):
        self.clean = clean

    def set_occupancy(self, occupancy):
        self.occupancy = occupancy

    def set_number(self, number):
        self.number = number

    def set_type(self, type):
        self.type = type


    def __repr__(self):
        return '<Room %r>' % self.number
