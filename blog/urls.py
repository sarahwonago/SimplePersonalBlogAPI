from django.urls import path
from .views import ArticleListCreateAPIView

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="list-create-articles")
]