from rest_framework import generics

from .models import Articles
from .serializers import ArticleSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Articles.object.public()
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Articles.object.public()
    serializer_class = ArticleSerializer