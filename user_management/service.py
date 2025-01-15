from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import password_changed
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import UserProfile
from user_management.messages import UserMessages
from user_management.serializers import UserSignupSerializer, UserLoginSerializer


class UserCreationService:

    def execute(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        password = validated_data.pop('password')
        user = serializer.create(validated_data)
        user.set_password(password)
        user.save()

        token = RefreshToken.for_user(user)
        data = serializer.data

        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return data

class UserLoginService:
    def execute(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserProfile.objects.filter(
            email = serializer.validated_data.get('email'),
            is_active = True
        ).first()

        if user.check_password(serializer.validated_data.get('password')):
            token = RefreshToken.for_user(user)
            data = {"refresh": str(token), "access": str(token.access_token)}
            return data
        raise ValidationError(UserMessages.ENTITY_DOES_NOT_EXIST)
