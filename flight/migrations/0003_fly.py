# Generated by Django 5.0.7 on 2024-09-28 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_remove_flight_airline_remove_flight_destination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=100)),
                ('flight_number', models.CharField(max_length=20)),
                ('departure_city', models.CharField(max_length=100)),
                ('arrival_city', models.CharField(max_length=100)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('duration', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]