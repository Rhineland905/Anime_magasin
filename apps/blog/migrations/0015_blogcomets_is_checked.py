# Generated by Django 4.1.3 on 2023-02-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_blogcomets_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomets',
            name='is_checked',
            field=models.BooleanField(default=False, verbose_name='Проверка'),
        ),
    ]
