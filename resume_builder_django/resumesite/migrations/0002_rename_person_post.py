# Generated by Django 4.0.3 on 2022-12-07 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Post',
        ),
    ]
