# Generated by Django 3.2.5 on 2024-06-17 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_color'),
        ('Wool', '0008_remove_wool_wool_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='WoolColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(default=0.0, verbose_name='العدد')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.color', verbose_name='اللون')),
                ('wool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Wool.wool', verbose_name='الخامة')),
            ],
        ),
    ]
