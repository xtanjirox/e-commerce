# Generated by Django 4.1 on 2022-12-15 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_front', '0002_alter_cart_table_alter_client_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'delivery',
            },
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_discount',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='payment_status',
            new_name='payment',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='status',
            new_name='payment_status',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps_front.delivery'),
            preserve_default=False,
        ),
    ]
