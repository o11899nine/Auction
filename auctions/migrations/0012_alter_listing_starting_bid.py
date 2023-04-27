# Generated by Django 4.2 on 2023-04-24 17:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0011_listing_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="starting_bid",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ]
            ),
        ),
    ]