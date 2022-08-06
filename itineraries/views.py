from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from itineraries.serializers import ItinerarySerializer, ItinerariesLegsSerializer
from itineraries.models import Itinerary, ItineraryLegs

from rest_framework.decorators import action

from itineraries.utils import transform_result

from itineraries.filters import DynamicSearchFilter, RangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from flights.paginations import StandardResultsSetPagination


class ItineraryView(ModelViewSet):
    serializer_class = ItinerarySerializer
    queryset = Itinerary.objects.all()
    filter_backends = (
        DynamicSearchFilter,
        DjangoFilterBackend,
    )
    filterset_class = RangeFilter
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=["get"], url_path="legs")
    def itineraries_legs(self, request: Request):

        itineraries_legs_queryset = ItineraryLegs.objects.all()

        itineraries_legs_serializer = ItinerariesLegsSerializer(
            data=itineraries_legs_queryset,
            many=True,
        )

        itineraries_legs_serializer.is_valid()

        return Response(transform_result(itineraries_legs_serializer.data))

    # @action(detail=False, methods=["get"], url_path="legs")
    # def itineraries_legs(self, request: Request):

    #     itinerary_queryset = Itinerary.objects.all()
    #     leg_queryset = Leg.objects.all()

    #     itinerary_serializer = ItinerarySerializer(
    #         data=itinerary_queryset,
    #         many=True,
    #     )
    #     itinerary_serializer.is_valid()
    #     leg_serializer = LegSerializer(
    #         data=leg_queryset,
    #         many=True,
    #     )
    #     leg_serializer.is_valid()
    #     # serializer = ItinerariesLegsSerializer(
    #     #     data={
    #     #         "legs": leg_serializer.data,
    #     #         # "itineraries": itinerary_serializer.data,
    #     #     },
    #     #     many=True,
    #     # )
    #     # serializer.is_valid()
    #     return Response(
    #         {
    #             "legs": leg_serializer.data,
    #             "itineraries": itinerary_serializer.data,
    #         },
    #     )
