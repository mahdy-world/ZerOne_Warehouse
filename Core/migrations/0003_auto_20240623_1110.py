# Generated by Django 3.2.5 on 2024-06-23 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modules',
            name='factory_active',
        ),
        migrations.RemoveField(
            model_name='modules',
            name='product_active',
        ),
        migrations.RemoveField(
            model_name='modules',
            name='supplier_active',
        ),
        migrations.RemoveField(
            model_name='modules',
            name='worker_active',
        ),
    ]