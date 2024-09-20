from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User Model.
    """

    class Meta:
        model = User
        fields = [
            "username",
            "email" 
        ]
        
class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Serializer for handling user registration.
    """

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password"
        ]
        extra_kwargs = {
            'password':{'write_only': True}
        }

class LoginSerializer(serializers.Serializer):
    """
    Serializer for handling user login.
    """

    username = serializers.CharField()
    password = serializers.CharField(
        write_only = True,
        style = {
            "input_type":"password"
        }
    )