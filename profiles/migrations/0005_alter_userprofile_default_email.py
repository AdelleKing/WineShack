# Generated by Django 3.2.25 on 2024-04-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userprofile_default_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_email',
            field=models.EmailField(default='SOME STRING', max_length=100),
        ),
    ]
