from django_fsm import FSMIntegerField

from core.constants import HealthStatus, Species, AdoptionStatus
from core.models import TimeStamp

from django.db import models


class Animal(TimeStamp):
    name = models.CharField(max_length=126, null=True, blank=True)
    breed = models.CharField(max_length=126, null=True, blank=True)
    health_status = models.CharField(choices=[(tag.name, tag.value) for tag in HealthStatus], null=True, blank=True)
    species = models.CharField(choices=[(tag.name, tag.value) for tag in Species], null=True, blank=True)
    is_active = models.BooleanField(default=True)
    status = FSMIntegerField(default=AdoptionStatus.PENDING.value)
    age =  models.IntegerField(null=True)


    def __str__(self):
        return f"{self.species} - {self.breed} - {self.name}"

