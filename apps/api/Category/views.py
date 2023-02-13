
from rest_framework import generics, permissions

from apps.api.Category.serializers import CategoryReadSerializer, CategoryWriteSerializer
from apps.catalog.models import Category


class CategoryListViews(generics.ListAPIView):
    serializer_class = CategoryReadSerializer
    queryset = Category.objects.all()

class CategoryDetailViews(generics.RetrieveAPIView):
    serializer_class = CategoryReadSerializer
    queryset = Category.objects.all()

class CategoryCreatViews(generics.CreateAPIView):
    serializer_class = CategoryWriteSerializer
    queryset = Category.objects.all()
    permissions_classes = [permissions.IsAdminUser]

class ProductUpdateViews(generics.UpdateAPIView):
    serializer_class = CategoryWriteSerializer
    queryset = Category.objects.all()
    permissions_classes = [permissions.IsAdminUser]

class ProductDeleteViews(generics.DestroyAPIView):
    serializer_class = CategoryWriteSerializer
    queryset = Category.objects.all()
    permissions_classes = [permissions.IsAdminUser]