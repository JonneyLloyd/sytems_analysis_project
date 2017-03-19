from app import app, db


class User_Details(db.Model):
    '''
    Database representation of a user
    '''
    __tablename__ = 'user_details'

    id = db.Column(db.Integer, primary_key=True)
    _first_name = db.Column(db.String(120), nullable=False)
    _last_name = db.Column(db.String(120), nullable=False)
    _contact_number = db.Column(db.Integer)
    


    def __init__(self, first_name, last_name, contact_number):
        self._first_name = first_name
        self._last_name = last_name
        self._contact_number = contact_number

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    @property
    def contact_number(self):
        return self._contact_number

    @first_name.setter
    def set_first_name(self, first_name):
        self._first_name = first_name

    @last_name.setter
    def set_last_name(self, last_name):
        self._last_name = last_name

    @email.setter
    def set_email(self, email):
        self._email = email

    @contact_number.setter
    def set_contact_number(self, contact_number):
        self._contact_number = contact_number

    def __repr__(self):
        return '<User %r>' % self.first_name
