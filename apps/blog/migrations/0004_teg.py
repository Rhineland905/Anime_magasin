# Generated by Django 4.1.3 on 2022-11-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teg', models.CharField(max_length=255, verbose_name='Тег')),
                ('article_table', models.ManyToManyField(to='blog.article')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Тег',
            },
        ),
    ]
