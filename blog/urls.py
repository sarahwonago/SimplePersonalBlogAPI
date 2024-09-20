from django.urls import path
from .views import (ArticleListCreateAPIView, ArticleDetailAPIView, ArticleListAPIView,
                    CommentCreateView, LikeArticleView, ShareArticleView)

urlpatterns = [
    path("featured-articles/", ArticleListAPIView.as_view(), name="featured-articles"),
    path("articles/", ArticleListCreateAPIView.as_view(), name="list-create-articles"),
    path("article/<uuid:pk>/", ArticleDetailAPIView.as_view(), name="article-detail"),
    path('articles/<uuid:pk>/comment/', CommentCreateView.as_view(), name='article-comment'),
    path('articles/<uuid:pk>/like/', LikeArticleView.as_view(), name='article-like'),
    path('articles/<uuid:pk>/share/', ShareArticleView.as_view(), name='article-share'),
]

