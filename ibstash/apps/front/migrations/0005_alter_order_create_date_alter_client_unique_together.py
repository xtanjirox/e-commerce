# Generated by Django 4.1 on 2022-12-15 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_front', '0004_order_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 15, 33, 54, 200077)),
        ),
        migrations.AlterUniqueTogether(
            name='client',
            unique_together={('client_phone', 'client_name')},
        ),
    ]
