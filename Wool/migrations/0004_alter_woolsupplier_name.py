# Generated by Django 3.2.5 on 2024-02-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wool', '0003_auto_20240211_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woolsupplier',
            name='name',
            field=models.CharField(max_length=50, verbose_name='إسم التاجر'),
        ),
    ]
