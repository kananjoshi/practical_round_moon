from django_fsm import FSMIntegerField

from core.constants import HealthStatus, Species, AdoptionStatus
from core.models import TimeStamp

from django.db import models


class AnimalAdoptions(TimeStamp):
    user = models.ForeignKey("UserProfile", null=True, blank=True, on_delete=models.DO_NOTHING)
    animal = models.ForeignKey("Animal",  null=True, blank=True, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=512, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    status = FSMIntegerField(default=AdoptionStatus.PENDING.value)

    def __str__(self):
        return f"{self.status}"
