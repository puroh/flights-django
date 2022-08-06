from inspect import classify_class_attrs

from django.db import models
from flights.mixins import MixinComunFields


class Leg(MixinComunFields):
    departure_airport = models.CharField(max_length=32)
    arrival_airport = models.CharField(max_length=32)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField(default=1)
    airline_name = models.CharField(max_length=32)
    airline_id = models.CharField(max_length=32)
    duration_mins = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.airline_name}"
