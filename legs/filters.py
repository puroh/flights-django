from legs.models import Leg
from rest_framework import filters

from django_filters.filterset import FilterSet
from django_filters.filters import DateTimeFromToRangeFilter


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist("search_fields", [])


class RangeFilter(FilterSet):
    created_at = DateTimeFromToRangeFilter()  # (lookup_expr="gte")
    # end_date = DateFilter(lookup_expr="lte")

    class Meta:
        model = Leg
        fields = ["created_at"]
