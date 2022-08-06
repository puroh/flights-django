from rest_framework.serializers import ModelSerializer, Serializer, PrimaryKeyRelatedField

from itineraries.models import Itinerary, ItineraryLegs
from legs.serializers import LegSerializer
from legs.models import Leg
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField


class ItinerarySerializer(ModelSerializer):
    legs = PresentablePrimaryKeyRelatedField(
        queryset=Leg.objects.all(),
        presentation_serializer=LegSerializer,
        many=True,
    )

    class Meta:
        model = Itinerary
        fields = [
            "id",
            "price",
            "coint",
            "agent",
            "agent_rating",
            "created_at",
            "updated_at",
            "legs",
        ]

        read_only_fields = ("id",)


class ItinerariesBasicSerializer(ModelSerializer):
    legs = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = [
            "id",
            "price",
            "coint",
            "agent",
            "agent_rating",
            "created_at",
            "updated_at",
            "legs",
        ]


class ItinerariesLegsSerializer(ModelSerializer):
    itineraries = ItinerariesBasicSerializer()
    legs = LegSerializer()

    class Meta:
        model = ItineraryLegs
        fields = ["itineraries", "legs"]
