# Generated by Django 3.2.25 on 2024-03-30 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240330_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ABV',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
