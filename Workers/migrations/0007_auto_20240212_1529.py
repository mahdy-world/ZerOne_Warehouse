# Generated by Django 3.2.5 on 2024-02-12 13:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Workers', '0006_auto_20240212_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerattendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 2, 12, 13, 29, 16, 480753, tzinfo=utc), verbose_name='تاريخ الحضور'),
        ),
        migrations.AlterField(
            model_name='workerpayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 2, 12, 13, 29, 16, 480753, tzinfo=utc), verbose_name='تاريخ السحب'),
        ),
        migrations.AlterField(
            model_name='workerproduction',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 2, 12, 13, 29, 16, 481740, tzinfo=utc), verbose_name='تاريخ الاستلام'),
        ),
    ]