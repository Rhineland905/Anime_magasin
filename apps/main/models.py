from django.db import models
from apps.main.mixins import MetaTagMixins
from tinymce.models import HTMLField
# Create your models here.


class Page(MetaTagMixins):
    name = models.CharField(verbose_name='Имя',max_length=255)
    slug = models.SlugField(unique=True)
    text = HTMLField(verbose_name='Содержания',null=True,blank=True)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Иформационая страница'
        verbose_name_plural = "Иформационые страницы"