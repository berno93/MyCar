# Generated by Django 3.1.6 on 2023-08-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCar', '0005_auto_20230811_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]