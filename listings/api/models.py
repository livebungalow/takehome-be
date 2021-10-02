from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# possible year range is between 1800 to 2100
YearValidator = [MinValueValidator(1800), MaxValueValidator(2100)]
# possible range of home price 0 to 1 billion
PriceValidator = [MinValueValidator(0), MaxValueValidator(10 ** 9)]


class ZillowData(models.Model):
    rent_estimate = models.FloatField(null=True, blank=True, validators=PriceValidator)
    rent_estimate_last_updated = models.DateField(null=True)
    estimate_amount = models.FloatField(null=True, blank=True, validators=PriceValidator)
    estimate_last_updated = models.DateField()
    zillow_id = models.IntegerField()
    link = models.TextField()

    def save(self, *args, **kwargs):
        super().clean_fields()
        super().save(*args, **kwargs)


class Address(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=50)
    zipcode = models.SlugField()
    state = models.CharField(max_length=50)


class Home(models.Model):
    area_unit = models.CharField(max_length=10, default='SqFt')
    bathrooms = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    bedrooms = models.IntegerField(validators=[MinValueValidator(0)])
    home_size = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    property_size = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    home_type = models.CharField(max_length=50)
    last_sold_date = models.DateField(null=True, blank=True)
    last_sold_price = models.FloatField(null=True, blank=True, validators=PriceValidator)
    rent_price = models.FloatField(null=True, blank=True, validators=PriceValidator)
    tax_value = models.FloatField()
    tax_year = models.IntegerField()
    year_built = models.IntegerField(null=True, blank=True, validators=YearValidator)
    price = models.IntegerField(validators=PriceValidator)
    zillow_data = models.ForeignKey(ZillowData, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().clean_fields()
        super().save(*args, **kwargs)

