# Generated by Django 3.2.5 on 2024-08-02 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0021_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 3, 0, 51, 1, 598825), verbose_name='التاريخ'),
        ),
    ]