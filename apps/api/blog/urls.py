
from rest_framework.routers import DefaultRouter

from apps.api.blog.views import BlogCategoryViewSet,ArticleViewSet

urlpatterns = []
router = DefaultRouter()
router.register('category', BlogCategoryViewSet, basename='category')
router.register('article', ArticleViewSet, basename='article')

urlpatterns += router.urls


