# Generated by Django 5.0.1 on 2024-03-08 21:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_reservation_date_reservation_is_accepted_and_more'),
        ('mainapp', '0004_remove_packages_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.hotel'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='rooms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.rooms'),
        ),
    ]
