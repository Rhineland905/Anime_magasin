from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.safestring import mark_safe

from apps.main.mixins import MetaTagMixins
from apps.user.models import User
from config.settings import MEDIA_ROOT


class BlogCategory(MetaTagMixins):
    name = models.CharField(verbose_name='Имя категории', max_length=255)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категории блога'

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description = 'Изображение'

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}>")

    image_tag_thumbnail.short_description = 'Изображение'


class Tag(MetaTagMixins):
    name = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(MetaTagMixins):
    category = models.ForeignKey(to=BlogCategory, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Текст-превью', null=True, blank=True)
    user = models.ForeignKey(to=User, verbose_name='Пользователь', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(verbose_name='Дата публикации')
    tags = models.ManyToManyField(to=Tag, verbose_name='Теги', blank=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/article/',
        null=True,
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)]
    )
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
