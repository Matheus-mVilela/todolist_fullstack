# Generated by Django 3.2.9 on 2021-11-12 20:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settaskmodel',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 12, 17, 38, 5, 643974)),
        ),
        migrations.AlterField(
            model_name='settaskmodel',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 12, 17, 38, 5, 643935)),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 12, 17, 38, 5, 645024)),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 12, 17, 38, 5, 644994)),
        ),
    ]