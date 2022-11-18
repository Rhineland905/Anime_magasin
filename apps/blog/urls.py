from apps.blog.views import blog_category_list
from django.urls import path

urlpatterns = [
    path('',blog_category_list,name="blog_category_list")
    ]

