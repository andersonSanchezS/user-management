# SimpleJWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Roles and permissions
from rolepermissions.roles import get_user_roles


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        roles = []
        token = super().get_token(user)
        for role in get_user_roles(user):
            roles.append(role.__name__.lower())

        # Add custom claims
        token['name'] = user.username
        token['roles'] = roles

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
