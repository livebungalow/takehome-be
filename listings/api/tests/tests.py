from django.test import TestCase
import pytest

from api import serializers as api_serializers
from api import models as api_models

pytestmark = pytest.mark.django_db

def create_new_home():
    data = {
        "address": "New Adr",
        "city": "Toronto",
        "state": "CA",
        "zipcode": "91307",
        "bathrooms": 1,
        "bedrooms": 4,
        "year_built": 2020,
        "tax_year": 2018,
        "tax_value": 5000,
        "home_size": 123,
        "lot_size": 1235,
        "estimate_amount": 1000000,
        "estimate_last_update": "2022-06-23",
        "market_price": "1M",
        "home_type": "SINGLE_FAMILY",
        "link": "https://www.test.com/testurl-2"
    }
    serializer = api_serializers.HomeSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    return instance

@pytest.mark.usefixtures("django_db_setup")
class TestHomes(TestCase):
    def test_home_data(self):
        home = api_models.Home.objects.get(id=0)
        self.assertEqual(home.city, "Toronto")

    def test_serializer(self):
        original = api_models.Home.objects.get(id=0)
        instance = create_new_home()
        self.assertNotEqual(original.address, instance.address)

@pytest.mark.usefixtures("django_db_setup")
class TestRentData(TestCase):
    def test_rent_data(self):
        rent_data = api_models.RentData.objects.get(id=0)
        self.assertEqual(rent_data.rent_estimate_price, 2500)

    def test_serializer(self):
        original = api_models.RentData.objects.get(id=0)
        home_instance = create_new_home()
        data = {
            "id": 1,
            "home": home_instance.id,
            "rent_price": 500,
            "rent_estimate_price": 200,
            "rent_estimate_last_update": "2022-06-21"
        }
        serializer = api_serializers.RentDataSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        self.assertNotEqual(original.home_id, instance.home_id)


@pytest.mark.usefixtures("django_db_setup")
class TestSaleData(TestCase):
    def test_sale_data(self):
        sale_data = api_models.SaleData.objects.get(id=0)
        self.assertEqual(sale_data.price, 100000000)
        
    def test_serializer(self):
        original = api_models.SaleData.objects.get(id=0)
        home_instance = create_new_home()
        data = {
            "home": home_instance.id,
            "listing_date": "2022-06-21",
            "sale_date": "2022-06-22",
            "price": 100000000
        }
        serializer = api_serializers.SaleDataSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        self.assertNotEqual(original.home_id, instance.home_id)