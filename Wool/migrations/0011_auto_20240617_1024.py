# Generated by Django 3.2.5 on 2024-06-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wool', '0010_alter_woolcolor_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='woolcolor',
            name='weight',
            field=models.FloatField(default=0.0, verbose_name='الوزن'),
        ),
        migrations.AlterField(
            model_name='woolcolor',
            name='count',
            field=models.FloatField(default=0.0, verbose_name='العدد'),
        ),
    ]