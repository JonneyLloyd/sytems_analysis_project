from app import app, db


class User(db.Model):
    '''
    Database representation of a user
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contact_number = db.Column(db.Integer)
    


    def __init__(self, first_name, last_name, email, contact_number):
        self.email = email

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email

    def set_contact_number(self, contact_number):
        self.contact_number = contact_number


    def __repr__(self):
        return '<User %r>' % self.first_name
