import csv
from django.core.management.base import BaseCommand, CommandError
from api.models import Listings


class Command(BaseCommand):
    help = 'Imports data about houses'

    def add_arguments(self, parser):
        # TODO: Add any arguments here
        # parser.add_argument('--path', type=str)
        pass

    def handle(self, *args, **options):
        # TODO: implement your import command
        with open('/Users/vdonaire/github_com/takehome-be/sample-data/data.csv') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                Listings.objects.create(
                    area_unit=row[0],
                    bathrooms=row[1],
                    bedrooms=row[2],
                    home_size=row[3],
                    home_type=row[4],
                    last_sold_date=row[5],
                    last_sold_price=row[6],
                    link=row[7],
                    price=row[8],
                    property_size=row[9],
                    rent_price=row[10],
                    rentzestimate_amount=row[11],
                    rentzestimate_last_updated=row[12],
                    tax_value=row[13],
                    tax_year=row[14],
                    year_built=row[15],
                    zestimate_amount=row[16],
                    zestimate_last_updated=row[17],
                    zillow_id=row[18],
                    address=row[19],
                    city=row[20],
                    state=row[21],
                    zipcode=row[22]                 
                )
        self.stdout.write("Data should have been imported")
