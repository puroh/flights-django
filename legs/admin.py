from django.contrib import admin
from legs.models import Leg


@admin.register(Leg)
class LegAdmin(admin.ModelAdmin):
    # fields = ()
    list_display = (
        "airline_name",
        "airline_id",
        "arrival_airport",
    )
