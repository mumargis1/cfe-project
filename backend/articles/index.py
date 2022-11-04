from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register


from .models import Articles


@register(Articles)
class ArticleIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'title',
        'body',
        'user',
        'publish_date',
        'path',
        'endpoint',
    ]
    settings = {
        'searchableAttributes': ['title', 'body'],
        'attributesForFaceting': ['user'],
        'ranking': ['asc(publish_date']
    }
    tags = 'get_tags_list'