
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.paginator import Paginator

from animal_management.adoption_services import AdoptionServices
from animal_management.messages import AnimalMessages
from animal_management.serializer import RetrieveAdoptionsRequests
from core.constants import AdoptionStatus
from core.models import AnimalAdoptions


class AnimalAdoptionManagementViews(ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = AnimalAdoptions.objects.all()
    filter_fields = (
       'status'
    )
    search_fields = (
       'status'
    )

    @transaction.atomic
    @action(detail=True, methods=["post"], name="adoption-requests", url_name="adoption-requests")
    def adoption_requests(self, request):
        obj = AdoptionServices().create_adoption(request)
        response = RetrieveAdoptionsRequests(obj).data
        return Response(data=response, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["list"], name="get-adoption-requests", url_name="get-adoption-requests")
    def get_adoption_requests(self, request):
        paginator = Paginator(self.queryset, request.GET.get("page_size"))
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        serializer = RetrieveAdoptionsRequests(page_obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["patch"], name="change-adoption-request", url_name="change-adoption-request")
    def change_adoption_request(self, request, pk):
        response = AdoptionServices().approve_reject_adoptions(request, pk)
        return Response(data=response, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], name="retrieve-adoption-request", url_name="retrieve-adoption-request")
    def retrieve_adoption_request(self, request, pk):
        obj = get_object_or_404(AnimalAdoptions, id=pk)
        response = RetrieveAdoptionsRequests(obj).data
        return Response(data=response, status=status.HTTP_200_OK)