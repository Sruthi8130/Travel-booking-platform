# Generated by Django 5.0.7 on 2024-10-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0008_fly_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fly',
            name='img',
            field=models.CharField(max_length=9999, null=True),
        ),
        migrations.AlterField(
            model_name='fly',
            name='travel_date',
            field=models.DateField(null=True),
        ),
    ]
