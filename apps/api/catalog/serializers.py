from rest_framework import serializers
from apps.catalog.models import Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(write_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'parent',
            'image',
            'meta_title',
            'meta_description',
            'meta_keywords',
        )


class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'quantity',
            'price',
        )

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id',
            'image',
            'product',
            'is_main'
        )

class ProductReadSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    images = ProductImageSerializer(many=True)
    main_image = ProductImageSerializer()
    class Meta:
        model = Product
        fields = (
            'id',
            'images',
            'main_image',
            'name',
            'slug',
            'description',
            'quantity',
            'price',
            'categories'
        )


