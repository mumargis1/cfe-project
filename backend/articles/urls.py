from django.urls import path

from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('', views.ArticleDetailView.as_view(), name='article-detail'),
]