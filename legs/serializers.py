from rest_framework.serializers import ModelSerializer

from legs.models import Leg


class LegSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Leg
