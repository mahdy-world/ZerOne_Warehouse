# Generated by Django 3.2.5 on 2024-01-08 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 0, 14, 53, 337001), verbose_name='التاريخ'),
        ),
    ]