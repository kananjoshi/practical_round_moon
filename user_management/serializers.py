from rest_framework import serializers

from core.models import UserProfile
from user_management.messages import UserMessages


class UserSignupSerializer(serializers.ModelSerializer):
    """
    This serializer is going to validate the fields provide for user registration
    """

    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'password', 'age')


class UserLoginSerializer(serializers.Serializer):
    """
    This serializer is going to validate the fields provide for user login
    """
    email = serializers.EmailField(
        required=True,
        error_messages={
            'required' : UserMessages.REQUIRED_FIELD
        }
    )
    password = serializers.CharField(
        required=True,
        error_messages={
            'required': UserMessages.REQUIRED_FIELD
        }
    )


