# Generated by Django 3.2.5 on 2024-06-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wool', '0009_woolcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woolcolor',
            name='count',
            field=models.FloatField(default=0.0, verbose_name='الوزن'),
        ),
    ]
