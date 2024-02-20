from django.db.models import Q
from django_filters import rest_framework as filters

from api import models as api_models


class RentDataFilters(filters.FilterSet):
    rent_estimate_update = filters.DateFromToRangeFilter(field_name="rent_estimate_last_update")
    rent_estimate_price = filters.BaseRangeFilter()

    class Meta:
        model = api_models.RentData
        fields = [
            "home_id",
            "rent_estimate_update",
            "rent_estimate_price"
        ]


class SaleDataFilters(filters.FilterSet):
    # Allows for searching between {field_name}_before and {field_name}_after in queries
    listing_date = filters.DateFromToRangeFilter()
    sale_date = filters.DateFromToRangeFilter()

    # Allows for range filtering with {val1},{val2} in queries
    price = filters.BaseRangeFilter()

    class Meta:
        model = api_models.SaleData
        fields = [
            "home_id",
            "listing_date",
            "sale_date",
            "price"
        ]

def by_location(queryset, name, value, *args, **kwargs):
    return queryset.filter(
        Q(address__icontains=value) |
        Q(city__icontains=value) |
        Q(state__icontains=value) |
        Q(zipcode__icontains=value)).distinct()

class HomeFilters(filters.FilterSet):
    
    location = filters.CharFilter(method=by_location)

    class Meta:
        model = api_models.Home
        fields = [
            "location"
        ]
