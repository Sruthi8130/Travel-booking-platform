# Generated by Django 5.0.7 on 2024-10-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_list_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='price',
        ),
        migrations.AddField(
            model_name='list',
            name='first_room_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='second_room_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='third_room_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
