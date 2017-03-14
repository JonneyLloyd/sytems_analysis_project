from app import app, db
from enum import Enum


class PermissionEnum(Enum):
    CAN_VIEW = 'CAN_VIEW'
    CAN_EDIT = 'CAN_EDIT'


class Permission(db.Model):
    '''
    Database representation of a permission
    '''
    __tablename__ = 'permission'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Permission %r>' % self.name
