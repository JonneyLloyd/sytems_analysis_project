from app import app, db
from enum import Enum

from app.models.permission import Permission, PermissionEnum


class RoleEnum(Enum):
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    GUEST = 'GUEST'
    ANONYMOUS = 'ANONYMOUS'


'''
Many to many relationship between roles and permissions
'''
role_permission = db.Table(
    'role_permission',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), nullable=False),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), nullable=False),
    db.PrimaryKeyConstraint('role_id', 'permission_id')
)


class Role(db.Model):
    '''
    Database representation of a role
    '''
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    permissions = db.relationship('Permission', secondary=role_permission, backref='roles')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name
