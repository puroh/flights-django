from django.db import models
from flights.mixins import MixinComunFields

from legs.models import Leg


class Itinerary(MixinComunFields):

    price = models.DecimalField(max_digits=6, decimal_places=2)
    coint = models.CharField(max_length=16)
    agent = models.CharField(max_length=32)
    agent_rating = models.DecimalField(max_digits=6, decimal_places=1)
    legs = models.ManyToManyField(
        Leg,
        through="ItineraryLegs",
        related_name="itineraries",
    )

    def __str__(self) -> str:
        return f"{self.agent}"


class ItineraryLegs(MixinComunFields):
    itineraries = models.ForeignKey(
        Itinerary,
        related_name="itinerary_legs",
        on_delete=models.CASCADE,
    )
    legs = models.ForeignKey(
        Leg,
        related_name="itinerary_legs",
        on_delete=models.CASCADE,
    )

    # class Meta:
    #     ordering = [""]
