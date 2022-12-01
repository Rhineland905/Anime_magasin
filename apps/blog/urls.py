from apps.blog.views import blog_category_list, article_list, article_viwe,teg_shear
from django.urls import path

urlpatterns = [
    path('', blog_category_list, name="blog_category_list"),
    path("<int:category_id>/", article_list, name="blog_article_list"),
    path("<int:category_id>/<int:article_id>/", article_viwe, name="blog_article_viwe"),
    path("<str:teg_id>", teg_shear, name="teg_view")
]
