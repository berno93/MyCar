# Generated by Django 3.1.6 on 2023-08-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpost',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
