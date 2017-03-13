from flask import g
from app.models.role import RoleEnum
from app.models.permission import PermissionEnum


class AccessManager(object):

    @staticmethod
    def user_is_role(role_name):
        if isinstance(role_name, RoleEnum):
            role_name = role_name.value
        return role_name == g.user.role.name

    @staticmethod
    def user_has_permission(permission_name):
        if isinstance(permission_name, PermissionEnum):
            permission_name = permission_name.value
        return permission_name in g.user.role.permissions
