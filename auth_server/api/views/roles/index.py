# Utils
import importlib
import inspect
# REST Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Permissions
from rolepermissions.decorators import has_permission_decorator
from rolepermissions.roles import assign_role, remove_role
# Models
from django.contrib.auth.models import User


@api_view(['GET'])
def roleList(request, *args, **kwargs):
    try:
        roles = []
        for name, cls in inspect.getmembers(importlib.import_module("Base.roles"), inspect.isclass):
            if name != "AbstractUserRole":
                roles.append(name.lower())
        return Response({'roles': roles}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@has_permission_decorator('update_user')
def addRole(request, pk):
    try:
        role = request.data['role']
        user = User.objects.get(pk=pk)
        assign_role(user, role)
        return Response({'message': 'Role added'}, status=status.HTTP_200_OK)
    except user.DoesNotExist:
        return Response({'Error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def deleteRole(request, pk):
    try:
        role = request.data['role']
        user = User.objects.get(pk=pk)
        remove_role(user, role)
        return Response({'message': 'Role deleted'}, status=status.HTTP_200_OK)
    except user.DoesNotExist:
        return Response({'Error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
