from rest_framework import serializers

from api.serializers import UserPublicSerializer
from .models import Articles


class ArticleSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)
    class Meta:
        model = Articles
        fields = [
            'pk',
            'author',
            'title',
            'body',
            'path',
            'endpoint',
        ]