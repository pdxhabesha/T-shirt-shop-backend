# Generated by Django 2.2 on 2019-05-25 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tshirtapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_attribute',
            new_name='attribute',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_category',
            new_name='category',
        ),
    ]
