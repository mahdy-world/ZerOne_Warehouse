# Generated by Django 3.2.5 on 2024-01-08 23:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 1, 5, 57, 265110), verbose_name='التاريخ'),
        ),
    ]