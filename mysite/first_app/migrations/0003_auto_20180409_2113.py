# Generated by Django 2.0.3 on 2018-04-09 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0002_auto_20180409_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=50)),
                ('product_category', models.CharField(blank=True, max_length=50)),
                ('product_description', models.CharField(blank=True, max_length=200)),
                ('add_time', models.TimeField(blank=True)),
                ('min_bid', models.PositiveIntegerField(blank=True)),
                ('time_limit', models.PositiveIntegerField(blank=True)),
                ('seller_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_age',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_phone_no',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
