from app import app, db
from sqlalchemy.ext.hybrid import hybrid_property


class UserDetails(db.Model):
    '''
    Database representation of a user
    '''
    __tablename__ = 'user_details'

    _id = db.Column('id', db.Integer, primary_key=True)
    _first_name = db.Column('first_name', db.String(120), nullable=False)
    _last_name = db.Column('last_name', db.String(120), nullable=False)
    _contact_number = db.Column('contact_number', db.Integer)

    def __init__(self, first_name, last_name, contact_number=None):
        self._first_name = first_name
        self._last_name = last_name
        self._contact_number = contact_number

    @hybrid_property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @hybrid_property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @hybrid_property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @hybrid_property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value

    def __repr__(self):
        return '<User %r>' % self.first_name
