# Generated by Django 3.2.5 on 2024-08-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wool', '0019_rename_operatoin_color_wooloperatoin_operation_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='wooloperatoin',
            name='operation_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='رقم العملية'),
        ),
    ]
