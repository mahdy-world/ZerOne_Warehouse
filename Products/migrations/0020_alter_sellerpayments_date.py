# Generated by Django 3.2.5 on 2024-08-02 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0019_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 2, 23, 26, 32, 247616), verbose_name='التاريخ'),
        ),
    ]
