# Generated by Django 5.0.7 on 2024-10-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_list_four_list_one_list_three_list_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='fifth',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='first',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='fourth',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='second',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='sixth',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='third',
            field=models.CharField(max_length=999, null=True),
        ),
    ]
