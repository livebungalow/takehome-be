from django.core.management.base import BaseCommand, CommandError
from django.db import models
import csv
from datetime import datetime

from api import models as api_models

column_conversions = {
    "last_sold_date": "sale_date",
    "property_size": "lot_size",
    "zestimate_amount": "estimate_amount",
    "zestimate_last_updated": "estimate_last_update",
    "rentzestimate_amount": "rent_estimate_price",
    "rentzestimate_last_updated": "rent_estimate_last_update",
    "last_sold_price": "price",
    "price": "market_price"
}

to_create_models = [
    api_models.Home,
    api_models.RentData,
    api_models.SaleData,
]

class Command(BaseCommand):
    help = 'Imports data about houses'

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the CSV to load into the Database")

    def get_fields(self, model):
        return model._meta.fields

    def handle(self, *args, **options):
        csv_path = options["file_path"]
        with open(csv_path, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            column_data = {}
            for row in reader:
                if len(column_data) == 0:
                    for i in range(len(row)):
                        data = row[i].replace(' ', '')
                        if data in column_conversions:
                            data = column_conversions[data]
                        column_data[data] = i
                    continue
                for model in to_create_models:
                    kwargs = {}
                    for field in self.get_fields(model):
                        field_name = field.name
                        if field_name in column_data:
                            data = row[column_data[field_name]]
                            if data and isinstance(field, models.fields.DateField):
                                data = datetime.strptime(data, '%m/%d/%Y')
                            kwargs[field_name] = data if data else None
                        if model == api_models.Home and field_name == "id":
                            data = row[column_data["zillow_id"]]
                            kwargs["id"] = data if data else None
                        
                        if field_name == "home":
                            data = row[column_data["zillow_id"]]
                            kwargs["home_id"] = data if data else None
                    model.objects.get_or_create(**kwargs)


                