from rest_framework.viewsets import ModelViewSet
from legs.serializers import LegSerializer
from legs.models import Leg
from legs.filters import DynamicSearchFilter, RangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from flights.paginations import StandardResultsSetPagination


class LegView(ModelViewSet):
    serializer_class = LegSerializer
    queryset = Leg.objects.all()
    filter_backends = (
        DynamicSearchFilter,
        DjangoFilterBackend,
    )
    filterset_class = RangeFilter
    pagination_class = StandardResultsSetPagination
