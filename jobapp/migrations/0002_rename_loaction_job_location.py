# Generated by Django 4.1.12 on 2023-10-21 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='loaction',
            new_name='location',
        ),
    ]
