from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from animal_management.messages import AnimalMessages
from animal_management.serializer import RequestAdoptionSerializer, RetrieveAdoptionsRequests
from core.constants import AdoptionStatus
from core.models import AnimalAdoptions


class AdoptionServices:
    def create_adoption(self, request):
        serializer = RequestAdoptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        adoption_req_obj = serializer.create(serializer.validated_data)
        adoption_req_obj.user = request.user
        adoption_req_obj.save()
        return adoption_req_obj

    def approve_reject_adoptions(self, request, pk):
        if not request.user.is_superuser:
            raise ValidationError(AnimalMessages.PERMISSION_DENIED)
        obj = get_object_or_404(AnimalAdoptions, id=pk)
        adoption_status = request.data.get("status")
        obj.status = AdoptionStatus(adoption_status).value
        obj.save()
        response = RetrieveAdoptionsRequests(obj).data
        return response
