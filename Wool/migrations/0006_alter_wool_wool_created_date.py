# Generated by Django 3.2.5 on 2024-02-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wool', '0005_alter_woolsupplierquantity_wool_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wool',
            name='wool_created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الاضافة'),
        ),
    ]
