from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'add_user': True,
        'update_user': True,
        'delete_user': True,
    }


class Regular(AbstractUserRole):
    available_permissions = {
        'view_user': True
    }

