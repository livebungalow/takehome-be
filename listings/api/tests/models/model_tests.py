from django.test import TestCase
from api.models import Home, Address, ZillowData
from django.core.exceptions import ValidationError


def create_sample_model_obj(cls, data):
    return cls.objects.create(**data)


class ModelTests(TestCase):
    def setUp(self):
        self.sample_address_data = {
            "id": 1,
            "address": "7417 Quimby Ave",
            "city": "West Hills",
            "zipcode": "91307",
            "state": "CA"
        }
        self.sample_zillow_data = {
            "id": 1,
            "rent_estimate": 2850.0,
            "rent_estimate_last_updated": "2018-08-07",
            "estimate_amount": 709630.0,
            "estimate_last_updated": "2018-08-07",
            "zillow_id": 19866015,
            "link": "https://www.zillow.com/homedetails/7417-Quimby-Ave-West-Hills-CA-91307/19866015_zpid/"
        }
        self.sample_home_data = {
            "bathrooms": 4.0,
            "bedrooms": 5,
            "home_size": 3073.0,
            "property_size": 53665.0,
            "home_type": "SingleFamily",
            "last_sold_date": "2018-03-21",
            "last_sold_price": 2060000.0,
            "rent_price": None,
            "tax_value": 1661374.0,
            "tax_year": 2017,
            "year_built": 1981,
            "price": 12000
        }

    def test_year_built_positive_integer_must_be_between_1800_and_2100(self):
        # expected completion date may be in future
        address_obj = create_sample_model_obj(Address, self.sample_address_data)
        zillow_obj = create_sample_model_obj(ZillowData, self.sample_zillow_data)

        sample_home_data = {
            "bathrooms": 4.0,
            "bedrooms": 5,
            "home_size": 3073.0,
            "property_size": 53665.0,
            "home_type": "SingleFamily",
            "last_sold_date": "2018-03-21",
            "last_sold_price": 2060000.0,
            "rent_price": None,
            "tax_value": 1661374.0,
            "tax_year": 2017,
            "year_built": 1600,
            "price": 12000,
            "address": address_obj,
            "zillow_data": zillow_obj
        }
        with self.assertRaises(ValidationError):
            create_sample_model_obj(Home, sample_home_data)

    def test_deleting_zillow_object_deletes_associated_home_obj(self):
        address_obj = create_sample_model_obj(Address, self.sample_address_data)
        zillow_obj = create_sample_model_obj(ZillowData, self.sample_zillow_data)
        self.sample_home_data['address'] = address_obj
        self.sample_home_data['zillow_data'] = zillow_obj
        create_sample_model_obj(Home, self.sample_home_data)
        zillow_obj.delete()
        self.assertTrue(len(Home.objects.all()) == 0)

    def test_deleting_address_object_deletes_associated_home_obj(self):
        address_obj = create_sample_model_obj(Address, self.sample_address_data)
        zillow_obj = create_sample_model_obj(ZillowData, self.sample_zillow_data)
        self.sample_home_data['address'] = address_obj
        self.sample_home_data['zillow_data'] = zillow_obj
        create_sample_model_obj(Home, self.sample_home_data)
        address_obj.delete()
        self.assertTrue(len(Home.objects.all()) == 0)

    def test_home_price_must_be_in_valid_range(self):
        address_obj = create_sample_model_obj(Address, self.sample_address_data)
        zillow_obj = create_sample_model_obj(ZillowData, self.sample_zillow_data)

        sample_home_data = {
            "bathrooms": 4.0,
            "bedrooms": 5,
            "home_size": 3073.0,
            "property_size": 53665.0,
            "home_type": "SingleFamily",
            "last_sold_date": "2018-03-21",
            "last_sold_price": 2060000.0,
            "rent_price": None,
            "tax_value": 1661374.0,
            "tax_year": 2017,
            "year_built": 1600,
            "price": -1,
            "address": address_obj,
            "zillow_data": zillow_obj
        }
        with self.assertRaises(ValidationError):
            create_sample_model_obj(Home, sample_home_data)

