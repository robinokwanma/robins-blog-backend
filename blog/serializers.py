from rest_framework import serializers
import bleach
from bleach import ALLOWED_TAGS
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    clean_content = serializers.SerializerMethodField()
    tags = serializers.StringRelatedField(many=True)
    author = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'slug',
            'clean_content',
            'image',
            'tags',
            'published_date',
            'author',
            'meta_title',
            'meta_description',
            # Add other fields if necessary
        ]

    def get_clean_content(self, obj):
        allowed_tags = list(ALLOWED_TAGS) + [
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'blockquote', 'strong', 'em', 'u', 's', 'ol', 'ul', 'li',
            'figure', 'figcaption', 'img',
        ]
        allowed_attrs = {
            '*': ['class', 'style'],
            'a': ['href', 'title'],
            'img': ['src', 'alt', 'title', 'width', 'height'],
        }

        return bleach.clean(obj.content, tags=allowed_tags, attributes=allowed_attrs, strip=True)

    def get_author(self, obj):
        return obj.author.first_name + ' ' + obj.author.last_name
