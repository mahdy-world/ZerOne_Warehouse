# Generated by Django 3.2.5 on 2024-01-07 20:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WoolSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الاضافة')),
                ('name', models.CharField(max_length=50, verbose_name='إسم المورد')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='رقم الهاتف')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='العنوان')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WoolSupplierQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ العملية')),
                ('date', models.DateField(default=datetime.date.today, null=True, verbose_name='التاريخ')),
                ('wool_type', models.IntegerField(choices=[(1, 'قطن'), (2, 'صوف'), (3, 'عجينة'), (4, 'سبن'), (5, 'لكرة'), (6, 'رمش'), (7, 'عصب'), (8, 'بلستر'), (9, 'استك')], verbose_name='نوع الخيط')),
                ('wool_weight', models.FloatField(default=0.0, verbose_name='الوزن بالكيلو')),
                ('wool_price', models.FloatField(default=0.0, verbose_name='سعر الكيلو')),
                ('total_account', models.FloatField(default=0.0, verbose_name='اجمالي الحساب')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='المسؤول')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Wool.woolsupplier', verbose_name='المورد')),
            ],
        ),
        migrations.CreateModel(
            name='WoolSupplierPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ العملية')),
                ('date', models.DateField(default=datetime.date.today, null=True, verbose_name='التاريخ')),
                ('value', models.FloatField(default=0.0, verbose_name='المبلغ')),
                ('reason', models.CharField(blank=True, max_length=250, null=True, verbose_name='الوصف/السبب')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='المسؤول')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Wool.woolsupplier', verbose_name='المورد')),
            ],
        ),
    ]
