# Generated by Django 5.0.7 on 2024-10-06 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0023_remove_fly_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fly',
            name='name',
        ),
        migrations.RemoveField(
            model_name='fly',
            name='slug',
        ),
    ]
