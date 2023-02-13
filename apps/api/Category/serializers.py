from rest_framework import serializers
from apps.catalog.models import Category, Product





class CategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'parent',
            'description',

        )

class CategoryReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'parent',
            'description',
        )
