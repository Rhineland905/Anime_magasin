# Generated by Django 4.1.3 on 2023-02-24 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_product_productset_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productset',
            old_name='is_active',
            new_name='si_active',
        ),
    ]
