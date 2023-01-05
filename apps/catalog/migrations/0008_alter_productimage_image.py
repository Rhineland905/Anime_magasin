# Generated by Django 4.1.3 on 2023-01-03 14:56

from django.db import migrations
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default=django.utils.timezone.now, upload_to='catalog/product/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
