# REST Framework Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Serializers
from auth_server.api.serializers.users.index import RegistrationSerializer


class RegistrationView(APIView):
    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                account = serializer.save()
                refresh = RefreshToken.for_user(account.user)
                data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'username': account.username,
                    'email': account.email}
                return Response(data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
