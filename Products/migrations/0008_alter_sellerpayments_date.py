# Generated by Django 3.2.5 on 2024-02-13 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 13, 41, 44, 398619), verbose_name='التاريخ'),
        ),
    ]