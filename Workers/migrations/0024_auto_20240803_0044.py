# Generated by Django 3.2.5 on 2024-08-02 22:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Workers', '0023_auto_20240803_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerattendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 2, 22, 44, 39, 361887, tzinfo=utc), verbose_name='تاريخ الحضور'),
        ),
        migrations.AlterField(
            model_name='workerpayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 2, 22, 44, 39, 363887, tzinfo=utc), verbose_name='تاريخ السحب'),
        ),
        migrations.AlterField(
            model_name='workerproduction',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 2, 22, 44, 39, 365887, tzinfo=utc), verbose_name='تاريخ الاستلام'),
        ),
    ]