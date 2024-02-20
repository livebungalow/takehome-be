from django.db import models
from api import enums

class Home(models.Model):
    link = models.URLField("Link", unique=True, null=False, blank=False)
    address = models.CharField("Address", max_length=255, unique=True, null=False, blank=False)
    city = models.CharField("City", max_length=255, null=False, blank=False)
    state = models.CharField("State", max_length=2, null=False, blank=False)
    zipcode = models.CharField("zipcode", max_length=255, null=False, blank=False)

    bathrooms = models.FloatField("Bathrooms", default=None, null=True)
    bedrooms = models.FloatField("Bedrooms")

    year_built = models.IntegerField("Build Year", null=True, blank=True)
    tax_year = models.IntegerField("Tax Year", default=None, null=True)
    tax_value = models.FloatField("Tax Value", default=None, null=True)

    home_size = models.IntegerField("Home Size", default=None, null=True)
    lot_size = models.IntegerField("Lot Size", default=None, null=True)

    area_unit = models.CharField("Area Unit", max_length=255, default="SqFt", null=False, blank=False)
    home_type = models.CharField("Home Type", max_length=255, choices=enums.HomeType.choices(), null=False, blank=False)

    estimate_amount = models.IntegerField("Estimate Amount", default=None, null=True)
    estimate_last_update = models.DateField()
    market_price = models.CharField("Area Unit", max_length=255, null=False, blank=False)


class RentData(models.Model):
    home = models.ForeignKey(Home, null=False, on_delete=models.CASCADE)

    rent_price = models.IntegerField("Rent Price", null=True, blank=True)
    rent_estimate_price = models.IntegerField("Rent Estimate", default=None, null=True)
    rent_estimate_last_update = models.DateField(null=True)


class SaleData(models.Model):
    home = models.ForeignKey(Home, null=False, on_delete=models.CASCADE)
    
    listing_date = models.DateField(null=True)
    sale_date = models.DateField(null=True)

    price = models.IntegerField(null=True)
