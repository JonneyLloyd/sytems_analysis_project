from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.role import Role, RoleEnum


class User(db.Model):
    '''
    Database representation of a login
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    _password_hash = db.Column(db.String(128), nullable=False)
    _email = db.Column(db.String(120), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    role = db.relationship('Role')

    def __init__(self, email):         
	self._email = email  
	self.set_role_id()
         

    @property
    def password_hash(self):
        return self._password_hash

    @property
    def role_id(self):
        return self._role_id

    @property
    def email(self):
        return self._email

    @email.setter
    def set_email(self, email):
        self._email = email

    @password_hash.setter
    def set_password_hash(self, password):
        self._password_hash = generate_password_hash(password)


    def verify_password(self, password):    # Should this be in the model?
        return check_password_hash(self.password_hash, password)

    def set_role(self, role_enum=None):    # Should this be in the model?
        default_role_name = RoleEnum.GUEST
        role_name = role_enum if role_enum is not None else default_role_name
        # check if valid role in enum??

        role = Role.query.filter_by(name=role_name.value).first()
        if not role:
            role = Role(name=role_name.value)
        self.role = role

    def __repr__(self):
        return '<User %r>' % self._id
