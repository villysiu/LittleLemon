# Generated by Django 5.0 on 2023-12-27 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_no_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
    ]