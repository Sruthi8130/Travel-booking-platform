# Generated by Django 5.0.7 on 2024-10-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0020_remove_fly_name_remove_fly_slug_fly_airline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fly',
            name='airline',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
