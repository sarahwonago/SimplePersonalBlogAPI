from django.urls import path
from .views import ArticleListCreateAPIView, ArticleDetailAPIView, ArticleListAPIView

urlpatterns = [
    path("featured-articles/", ArticleListAPIView.as_view(), name="featured-articles"),
    path("articles/", ArticleListCreateAPIView.as_view(), name="list-create-articles"),
    path("article/<uuid:pk>/", ArticleDetailAPIView.as_view(), name="article-detail"),
]