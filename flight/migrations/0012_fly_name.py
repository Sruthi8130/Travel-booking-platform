# Generated by Django 5.0.7 on 2024-10-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0011_remove_fly_name_remove_fly_slug_fly_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='fly',
            name='name',
            field=models.TextField(max_length=99, null=True),
        ),
    ]
