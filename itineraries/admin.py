from django.contrib import admin
from itineraries.models import Itinerary


@admin.register(Itinerary)
class LegAdmin(admin.ModelAdmin):
    # fields = ()
    list_display = (
        "agent",
        "agent_rating",
        "price",
        "currency",
    )
