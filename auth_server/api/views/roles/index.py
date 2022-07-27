# Utils
import importlib
import inspect
# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Permissions
from rolepermissions.decorators import has_permission_decorator


@api_view(['GET'])
@has_permission_decorator('view_role')
def roleList(request, *args, **kwargs):
    try:
        roles = []
        for name, cls in inspect.getmembers(importlib.import_module("Base.roles"), inspect.isclass):
            if name != "AbstractUserRole":
                roles.append(name.lower())
        return Response({'roles': roles}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)