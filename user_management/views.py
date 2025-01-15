from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.models import UserProfile
from user_management.service import UserCreationService, UserLoginService


class UserManagementViews(ViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []
    queryset = UserProfile.objects.all()

    @action(detail=True, methods=["post"], name="signup", url_name="signup")
    def signup(self, request):
        response = UserCreationService().execute(request)
        return Response(data=response, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"], name="login", url_name="login")
    def login(self, request):
        response = UserLoginService().execute(request)
        return Response(data=response, status=status.HTTP_200_OK)
