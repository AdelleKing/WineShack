# Generated by Django 3.2.25 on 2024-04-03 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
