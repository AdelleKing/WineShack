# Generated by Django 3.2.25 on 2024-04-07 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_default_fullname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_fullname',
            new_name='default_full_name',
        ),
    ]