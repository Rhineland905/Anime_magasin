from django.contrib import admin
from apps.blog.models import BlogCategory
from apps.blog.models import Article

admin.site.register(BlogCategory)
admin.site.register(Article)
# Register your models here.
