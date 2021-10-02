import os
import re

import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'listings.settings')
django.setup()

from api.models import Home, Address, ZillowData

dir = os.path.abspath(os.getcwd())
path = os.path.join(dir.rsplit('/', 4)[0], 'sample-data/data.csv')
df = pd.read_csv(path)

last_sold_date = pd.to_datetime(df['last_sold_date'])
rentzestimate_last_updated = pd.to_datetime(df['rentzestimate_last_updated'])
zestimate_last_updated = pd.to_datetime(df['zestimate_last_updated'])
df['last_sold_date'] = last_sold_date
df['rentzestimate_last_updated'] = rentzestimate_last_updated
df['zestimate_last_updated'] = zestimate_last_updated


def populate_tables(df, size=None):
    if size:
        df = df.loc[:size]
    for i in df.index:
        row_data = df.loc[i].to_dict()
        for key, val in row_data.items():
            if str(val) in ('nan', 'NaT'):
                row_data[key] = None
        if row_data['price'].endswith('K'):
            price = int(re.findall(r'\d+', row_data['price'])[0]) * 1000
            row_data['price'] = price
        elif row_data['price'].endswith('M'):
            price = int(re.findall(r'\d+', row_data['price'])[0]) * 1000000
            row_data['price'] = price

        address = Address.objects.create(
            address=row_data['address'],
            city=row_data['city'],
            zipcode=row_data['zipcode'],
            state=row_data['state']
        )
        zillow_data = ZillowData.objects.create(
            rent_estimate=row_data['rentzestimate_amount'],
            rent_estimate_last_updated=row_data['rentzestimate_last_updated'],
            estimate_amount=row_data['zestimate_amount'],
            estimate_last_updated=row_data['zestimate_last_updated'],
            zillow_id=row_data['zillow_id'],
            link=row_data['link']
        )

        home = Home.objects.create(
            area_unit=row_data[' area_unit'],
            bathrooms=row_data['bathrooms'],
            bedrooms=row_data['bedrooms'],
            home_size=row_data['home_size'],
            property_size=row_data['property_size'],
            home_type=row_data['home_type'],
            last_sold_date=row_data['last_sold_date'],
            last_sold_price=row_data['last_sold_price'],
            rent_price=row_data['rent_price'],
            tax_value=row_data['tax_value'],
            tax_year=row_data['tax_year'],
            year_built=int(row_data['year_built']) if row_data['year_built'] else None,
            price=row_data['price'],
            address=address,
            zillow_data=zillow_data
        )
        print(home)


populate_tables(df)
