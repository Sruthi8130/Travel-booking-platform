# Generated by Django 5.0.7 on 2024-10-06 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=99, null=True)),
                ('slug', models.SlugField(max_length=99, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=99, null=True)),
                ('slug', models.SlugField(max_length=99, null=True)),
                ('place', models.CharField(max_length=100)),
                ('check_date', models.DateField(null=True)),
                ('check_time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img', models.CharField(max_length=9999)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.hotels')),
            ],
        ),
    ]
