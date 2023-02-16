from rest_framework import serializers
from apps.blog.models import Article , BlogCategory


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = (
            'id',
            'name',
            'image',
        )

class BlogArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'name',
            'text_preview',
            'user',
            'text',
            'tags',
            'image',
        )