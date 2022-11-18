from django.contrib import admin
from apps.blog.models import BlogCategory
from apps.blog.models import Article , Teg

admin.site.register(BlogCategory)
admin.site.register(Article)
admin.site.register(Teg)
# Register your models here.
