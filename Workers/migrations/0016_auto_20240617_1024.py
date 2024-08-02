# Generated by Django 3.2.5 on 2024-06-17 08:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Workers', '0015_auto_20240617_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerattendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 17, 8, 24, 18, 272198, tzinfo=utc), verbose_name='تاريخ الحضور'),
        ),
        migrations.AlterField(
            model_name='workerpayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 17, 8, 24, 18, 273196, tzinfo=utc), verbose_name='تاريخ السحب'),
        ),
        migrations.AlterField(
            model_name='workerproduction',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 17, 8, 24, 18, 274196, tzinfo=utc), verbose_name='تاريخ الاستلام'),
        ),
    ]
