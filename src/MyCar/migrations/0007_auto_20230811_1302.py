# Generated by Django 3.1.6 on 2023-08-11 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyCar', '0006_auto_20230811_1259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carpost',
            options={'ordering': ['-created_on'], 'verbose_name': 'Voiture'},
        ),
    ]
