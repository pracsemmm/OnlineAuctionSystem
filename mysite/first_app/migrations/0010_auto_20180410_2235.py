# Generated by Django 2.0.4 on 2018-04-10 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_customer_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='add_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 4, 10, 22, 35, 59, 546469)),
        ),
    ]
