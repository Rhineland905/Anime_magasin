from rest_framework import permissions, viewsets

from apps.api.blog.serializers import BlogCategorySerializer, BlogArticleSerializer
from apps.blog.models import BlogCategory, Article




class BlogCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = BlogCategorySerializer
    queryset = BlogCategory.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permission() for permission in [permissions.IsAdminUser]]
        return [permission() for permission in [permissions.AllowAny]]

class BlogArticleViewSet(viewsets.ModelViewSet):
    serializer_class = BlogArticleSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        category = self.request.query_params.get('category')
        name = self.request.query_params.get('name')
        if user:
            queryset = Article.objects.filter(user=user)
        if category:
            queryset = Article.objects.filter(category=category)
        if name:
            queryset = Article.objects.filter(name__icontains=name)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_permissions(self):

        if self.action in ['create', 'update', 'destroy']:
            return [permission() for permission in [permissions.IsAdminUser]]
        return [permission() for permission in [permissions.AllowAny]]