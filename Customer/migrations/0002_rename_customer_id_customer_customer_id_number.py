# Generated by Django 3.2.5 on 2024-06-23 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_id',
            new_name='customer_id_number',
        ),
    ]
