# Generated by Django 3.2.5 on 2024-08-09 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0027_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 9, 12, 11, 57, 537136), verbose_name='التاريخ'),
        ),
    ]
