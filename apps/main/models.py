
from django.db import models

from apps.catalog.models import Product
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

class ProductSet(models.Model):
    products = models.ManyToManyField(Product,verbose_name='Товары')
    name = models.CharField(verbose_name='Названия',max_length=255)
    sort = models.PositiveIntegerField(verbose_name='Сортировкак',default=0)
    si_active = models.BooleanField(verbose_name='Активиравано',default=True)\

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort']
        verbose_name = 'Карусель товара'
        verbose_name_plural = 'Карусель товарорв'