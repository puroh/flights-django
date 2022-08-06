from django.contrib import admin
from itineraries.models import Itinerary
from legs.models import Leg


class ItinerariesInline(admin.TabularInline):
    model = Leg.itineraries.through
    extra = 3


@admin.register(Itinerary)
class LegAdmin(admin.ModelAdmin):
    # fields = ()
    inlines = [
        ItinerariesInline,
    ]
    list_display = (
        "agent",
        "agent_rating",
        "price",
        "currency",
    )
