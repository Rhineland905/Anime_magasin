from django.core.checks import Tags
from rest_framework import serializers
from apps.blog.models import Article , BlogCategory, Tag


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
        )


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = (
            'id',
            'name',
            'image',
        )

class ArticleWriteSerializer(serializers.ModelSerializer):
    tags = serializers.ListSerializer(child=serializers.CharField(max_length=64), write_only=True)
    class Meta:
        model = Article
        fields = (
            'id',
            'name',
            'text_preview',
            'text',
            'publish_date',
            'image',
            'tags'
        )


class ArticleReadSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer()
    tags = TagsSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'name',
            'user',
            'text_preview',
            'text',
            'publish_date',
            'image',
            'category',
            # 'image_thumbnail',
            'created_at',
            'tags'
        )