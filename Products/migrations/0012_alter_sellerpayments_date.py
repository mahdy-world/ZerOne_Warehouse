# Generated by Django 3.2.5 on 2024-06-12 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 12, 8, 11, 2, 248646), verbose_name='التاريخ'),
        ),
    ]