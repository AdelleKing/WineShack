# Generated by Django 3.2.25 on 2024-04-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_fullname',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
