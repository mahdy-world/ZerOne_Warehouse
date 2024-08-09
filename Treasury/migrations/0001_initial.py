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
            name='Treasury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم الخزنة')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الاضافة')),
                ('balance', models.FloatField(default=0.0, verbose_name='رصيد الخزنة')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TreasuryOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_type', models.IntegerField(choices=[(1, 'اضافة رصيد'), (2, 'سحب رصيد')], default=0, verbose_name='نوع العملية')),
                ('operation_value', models.FloatField(default=0.0, verbose_name='قيمة العملية')),
                ('operation_description', models.TextField(blank=True, max_length=200, null=True, verbose_name='وصف العملية')),
                ('operation_date', models.DateTimeField(default=datetime.date.today, verbose_name='تاريخ العملية')),
                ('deleted_operation', models.BooleanField(default=False)),
                ('operation_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='انشاء بواسطة')),
                ('treasury', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Treasury.treasury', verbose_name='الخزنة')),
            ],
        ),
    ]