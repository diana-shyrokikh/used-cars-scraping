# Generated by Django 4.2.6 on 2023-10-10 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_vin',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
