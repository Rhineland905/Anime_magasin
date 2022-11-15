from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(verbose_name='Имя категории',max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категории блога'


class Article(models.Model):
    category = models.ForeignKey(to=BlogCategory,on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок',max_length=255)
    text_preview = models.TextField(verbose_name= 'Текст-привью',null=True,blank=True)
    text = models.TextField(verbose_name= 'Текст-привью')
    publish_date = models.DateTimeField(verbose_name='Дата публикацыи')
    updated_at = models.DateTimeField(verbose_name='Дата изменения',auto_now=True)
    created_at = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статья'