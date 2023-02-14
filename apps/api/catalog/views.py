from rest_framework import generics, permissions, viewsets
from apps.catalog.models import Category, Product, ProductImage
from apps.api.catalog.serializers import CategorySerializer, ProductReadSerializer, ProductWriteSerializer


class ProductListViews(generics.ListAPIView):
    serializer_class = ProductReadSerializer
    queryset = Product.objects.all()

class ProductDetailViews(generics.RetrieveAPIView):
    serializer_class = ProductReadSerializer
    queryset = Product.objects.all()

class ProductCreatViews(generics.CreateAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permissions_classes = [permissions.IsAdminUser]

class ProductUpdateViews(generics.UpdateAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permissions_classes = [permissions.IsAdminUser]

class ProductDeleteViews(generics.DestroyAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permissions_classes = [permissions.IsAdminUser]



class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.action['create','update','destroy']:
            return [permissions() for permissions in [permissions.IsAdminUser]]
        return [permissions() for permissions in [permissions.AllowAny]]

