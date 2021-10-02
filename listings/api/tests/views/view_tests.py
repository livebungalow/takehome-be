from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory
from api.tests.models.model_tests import create_sample_model_obj
from api.models import Home, Address, ZillowData
from api.views import HomeList


class ViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = HomeList.as_view()
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
        self.sample_home_data1 = {
            "bathrooms": 4.0,
            "bedrooms": 5,
            "home_size": 3073.0,
            "property_size": 53665.0,
            "home_type": "SingleFamily",
            "last_sold_date": "2015-03-21",
            "last_sold_price": 2060000.0,
            "rent_price": None,
            "tax_value": 1661374.0,
            "tax_year": 2017,
            "year_built": 1990,
            "price": 12000
        }

    def test_can_filter_by_year_built(self):
        address_obj = create_sample_model_obj(Address, self.sample_address_data)
        zillow_obj = create_sample_model_obj(ZillowData, self.sample_zillow_data)
        self.sample_home_data['address'] = address_obj
        self.sample_home_data['zillow_data'] = zillow_obj
        create_sample_model_obj(Home, self.sample_home_data)
        self.sample_home_data1['address'] = address_obj
        self.sample_home_data1['zillow_data'] = zillow_obj
        create_sample_model_obj(Home, self.sample_home_data1)
        request = self.factory.get('api/homes/?year_built=1990')
        response = self.view(request)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['year_built'], 1990)

    def test_can_filter_by_date_range(self):
        address_obj = create_sample_model_obj(Address, self.sample_address_data)
        zillow_obj = create_sample_model_obj(ZillowData, self.sample_zillow_data)
        self.sample_home_data['address'] = address_obj
        self.sample_home_data['zillow_data'] = zillow_obj
        create_sample_model_obj(Home, self.sample_home_data)
        self.sample_home_data1['address'] = address_obj
        self.sample_home_data1['zillow_data'] = zillow_obj
        create_sample_model_obj(Home, self.sample_home_data1)
        request = self.factory.get('api/homes/?last_sold_date__range=2014-12-18, 2015-12-20')
        response = self.view(request)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['last_sold_date'], '2015-03-21')
