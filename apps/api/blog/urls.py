from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api.blog.views import BlogCategoryViewSet,BlogArticleViewSet

urlpatterns = []
router = DefaultRouter()
router.register('category', BlogCategoryViewSet, basename='category')
router.register('article', BlogArticleViewSet, basename='article')

urlpatterns += router.urls


