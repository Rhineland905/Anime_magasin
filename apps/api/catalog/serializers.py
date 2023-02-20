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


class ProductReadSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'quantity',
            'price',
            'categories'
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