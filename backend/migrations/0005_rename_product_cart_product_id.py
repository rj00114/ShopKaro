# Generated by Django 3.2.5 on 2021-10-26 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='product_id',
        ),
    ]
