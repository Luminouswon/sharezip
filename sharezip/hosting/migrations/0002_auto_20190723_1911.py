# Generated by Django 2.2.3 on 2019-07-23 10:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 23, 10, 11, 26, 486975, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='room',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 23, 10, 11, 26, 486975, tzinfo=utc)),
        ),
    ]
