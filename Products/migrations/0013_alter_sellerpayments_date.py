# Generated by Django 3.2.5 on 2024-06-14 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0012_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 14, 8, 14, 10, 361446), verbose_name='التاريخ'),
        ),
    ]