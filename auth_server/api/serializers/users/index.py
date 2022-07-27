# REST framework
from rest_framework import serializers
# Models
from django.contrib.auth.models import User

# Role serializer
from rolepermissions.roles import assign_role


# Register a user
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    role = serializers.CharField(style={'input_type': 'text'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2','role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'write_only': True}
        }

    # Validations
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'Email': 'Email already exists'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        user = User.objects.get(id=account.id)
        try:
            assign_role(user, self.validated_data['role'])
        except Exception as e:
            user.delete()
            raise serializers.ValidationError('invalid role')
        return account
