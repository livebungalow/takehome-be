# Generated by Django 3.2.16 on 2022-11-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20221121_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='last_sold_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='listings',
            name='rentzestimate_last_updated',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='listings',
            name='zestimate_last_updated',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]