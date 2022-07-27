from rest_framework import permissions
from rolepermissions.checkers import has_permission


class PermissionsDecorator(permissions.BasePermission):
    def has_permission(self, request, view):
        userPermission = request.user.get_permissions()
        print(userPermission)
        return True
