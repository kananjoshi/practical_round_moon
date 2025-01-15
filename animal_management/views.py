
from django.db import transaction
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.paginator import Paginator

from animal_management.adoption_services import AdoptionServices
from animal_management.serializer import RetrieveAnimalDetails, RetrieveAdoptionsRequests
from animal_management.service import AnimalServices
from core.models import Animal, AnimalAdoptions


class AnimalManagementViews(ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Animal.objects.all()
    filter_fields = (
        'name',
        'species',
        'breed'
    )
    search_fields = (
        'name',
        'species',
        'breed'
    )

    @transaction.atomic
    @action(detail=True, methods=["post"], name="add-animal", url_name="add-animal")
    def add_animal(self, request):
        response = AnimalServices().execute(request)
        return Response(data=response, status=status.HTTP_201_CREATED)

    def get(self, request):
        paginator = Paginator(self.queryset, request.GET.get("page_size"))
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        serializer = RetrieveAnimalDetails(page_obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    @action(detail=True, methods=["post"], name="adoption-requests", url_name="adoption-requests")
    def adoption_requests(self, request):
        obj = AdoptionServices().create_adoption(request)
        response = RetrieveAdoptionsRequests(obj).data
        return Response(data=response, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["get"], name="get-adoption-requests", url_name="get-adoption-requests")
    def get_adoption_requests(self, request):
        queryset = AnimalAdoptions.objects.all()
        paginator = Paginator(queryset, request.GET.get("page_size"))
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        serializer = RetrieveAdoptionsRequests(page_obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)