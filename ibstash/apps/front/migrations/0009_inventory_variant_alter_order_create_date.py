# Generated by Django 4.1 on 2022-12-19 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps_front", "0008_product_category_alter_order_create_date_inventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventory",
            name="variant",
            field=models.ManyToManyField(to="apps_front.variant"),
        ),
        migrations.AlterField(
            model_name="order",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 19, 9, 7, 5, 521201)
            ),
        ),
    ]
