# Generated by Django 4.1.3 on 2023-02-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_product_user'),
        ('main', '0002_alter_page_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Названия')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='Сортировкак')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активиравано')),
                ('product', models.ManyToManyField(to='catalog.product', verbose_name='Товары')),
            ],
            options={
                'verbose_name': 'Карусель товара',
                'verbose_name_plural': 'Карусель товарорв',
                'ordering': ['sort'],
            },
        ),
    ]
