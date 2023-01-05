# Generated by Django 4.1.3 on 2023-01-03 14:30

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_productcategory_product_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='catalog/product/', verbose_name='Изображение')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основание изображения')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'Изображение товара',
                'verbose_name_plural': 'Изображения товара',
            },
        ),
    ]
