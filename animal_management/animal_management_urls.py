from django.urls import path

from animal_management.adoption_view import AnimalAdoptionManagementViews
from animal_management.views import AnimalManagementViews


urlpatterns = [
    path("", AnimalManagementViews.as_view({"get": "get"}), name=""),
    path(
        "add-animal/",
        AnimalManagementViews.as_view({"post": "add_animal"}),
        name="add-animal",
    ),
    path(
        "adoption-requests/",
        AnimalAdoptionManagementViews.as_view({"post": "adoption_requests"}),
        name="adoption-requests",
    ),
    path(
        "get-adoption-requests/",
        AnimalAdoptionManagementViews.as_view({"list": "get_adoption_requests"}),
        name="get-adoption-requests",
    ),
    path(
        "change-adoption-request/<int:pk>/",
        AnimalAdoptionManagementViews.as_view({"patch": "change_adoption_request"}),
        name="change-adoption-request/",
    ),
    path(
        "retrieve-adoption-request/<int:pk>/",
        AnimalAdoptionManagementViews.as_view({"get": "retrieve_adoption_request"}),
        name="retrieve-adoption-request/",
    ),
]
