# Generated by Django 4.1 on 2022-12-19 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps_front", "0006_variant_alter_order_create_date_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 19, 8, 44, 21, 265310)
            ),
        ),
        migrations.AlterModelTable(
            name="category",
            table="category",
        ),
        migrations.AlterModelTable(
            name="variant",
            table="variant",
        ),
    ]
