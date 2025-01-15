from django.contrib.auth.decorators import login_required
from rest_framework.exceptions import ValidationError

from animal_management.messages import AnimalMessages
from animal_management.serializer import CreateAnimalSerializer, RetrieveAnimalDetails


class AnimalServices:

    def execute(self, request):
        serializer = CreateAnimalSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        if not request.user.is_superuser:
            raise ValidationError(AnimalMessages.PERMISSION_DENIED)
        obj = serializer.save()
        return RetrieveAnimalDetails(obj).data


