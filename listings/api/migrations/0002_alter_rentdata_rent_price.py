# Generated by Django 3.2.24 on 2024-02-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentdata',
            name='rent_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rent Price'),
        ),
    ]