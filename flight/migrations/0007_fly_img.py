# Generated by Django 5.0.7 on 2024-09-30 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_alter_flight_slug_alter_fly_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='fly',
            name='img',
            field=models.CharField(blank=True, max_length=9999, null=True),
        ),
    ]