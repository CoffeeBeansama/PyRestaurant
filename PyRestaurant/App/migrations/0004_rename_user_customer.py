# Generated by Django 4.2.7 on 2024-01-13 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
    ]
