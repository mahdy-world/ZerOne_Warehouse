# Generated by Django 3.2.5 on 2024-08-10 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0030_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 10, 17, 19, 52, 291383), verbose_name='التاريخ'),
        ),
    ]