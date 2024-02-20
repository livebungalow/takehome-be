from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin

from api import models

class HomeSerializer(QueryFieldsMixin,
                     serializers.ModelSerializer):
    class Meta:
        model = models.Home
        # Choosing to be explicit with the fields here as it
        # makes it easier to see what is available for this serializer
        fields = [
            "id",
            "link",
            "address",
            "city",
            "state",
            "zipcode",
            "bathrooms",
            "bedrooms",
            "year_built",
            "tax_year",
            "tax_value",
            "home_size",
            "lot_size",
            "area_unit",
            "home_type",
            "estimate_amount",
            "estimate_last_update",
            "market_price"
        ]

class RentDataSerializer(QueryFieldsMixin,
                         serializers.ModelSerializer):

    class Meta:
        model = models.RentData
        fields = [
            "id",
            "rent_price",
            "rent_estimate_price",
            "rent_estimate_last_update",
            "home"
        ]

class SaleDataSerializer(QueryFieldsMixin,
                         serializers.ModelSerializer):
    
    class Meta:
        model = models.SaleData
        fields = [
            "id",
            "listing_date",
            "sale_date",
            "price",
            "home"
        ]