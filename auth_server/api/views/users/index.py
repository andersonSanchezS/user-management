# REST Framework Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Serializers
from auth_server.api.serializers.users.index import RegistrationSerializer

# Permissions
from rolepermissions.decorators import has_permission_decorator

# Models
from django.contrib.auth.models import User


@api_view(['POST'])
def registerUser(request):
    try:
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            refresh = RefreshToken.for_user(account)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': account.username,
                'email': account.email}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@has_permission_decorator('delete_user')
def deleteUser(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'message': 'User deleted'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PATCH'])
@has_permission_decorator('update_user')
def updateUser(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.username = request.data['username'] if request.data['username'] else user.username
        print(request.data)
        if request.data['password'] != "":
            user.set_password(request.data['password'])
        user.save()
        return Response({'message': 'User updated'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
