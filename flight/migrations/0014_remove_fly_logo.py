# Generated by Django 5.0.7 on 2024-10-02 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0013_fly_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fly',
            name='logo',
        ),
    ]
