from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .models import Article, Comment, Like, Share
from .serializers import ArticleSerializer, CommentSerializer, LikeSerializer, ShareSerializer
from .permissions import IsOwner

class ArticleListAPIView(APIView):
    """
    Handles retrieving a list of all articles that are featured.
    Supports query parameters 'tags' and published_date.

    Users must be authenticated.

    Methods:
        get: fetches a list of all articles.
    """

    permission_classes = [IsAuthenticated]

    @extend_schema(
            description="Retrieves a list of all featured articles."
    )
    def get(self, request):
        """
        Retrieves all the articles that are featured.
        """
        tags = request.query_params.get('tags', None)
        published_date = request.query_params.get('published_date', None)

        # Start with all featured articles
        articles = Article.objects.filter(featured=True)

        # Filter by tags if provided
        if tags:
            articles = articles.filter(tags__icontains=tags)

        # Filter by published_date if provided
        if published_date:
            articles = articles.filter(published_date__date=published_date)

        if tags and published_date:
            articles = articles.filter(Q(published_date__date=published_date)|Q(tags__icontains=tags))

        if not articles.exists():
            response = {
                "message":"No featured articles."
            }

            return Response(response, status=status.HTTP_200_OK)
        
        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ArticleListCreateAPIView(APIView):
    """
    Handles retrieving a list of articles and creating new articles.

    Users must be authenticated.

    Methods:
        get: fetches a list of all articles for a specific user.
        post: creates a new article.
    """

    permission_classes = [IsAuthenticated, IsOwner]


    def get(self, request):
        """
        Retrieves all the articles for the authenticated user.
        """
        articles = Article.objects.filter(user=request.user)

        if not articles.exists():
            response = {
                "message":"You have no articles."
            }

            return Response(response, status=status.HTTP_200_OK)
        
        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Creates a new article for the authenticated user.
        """

        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    """
    Handles retrieving, updating and deleting of a single article.

    Users must be authenticated.

    Methods:
        get: fetches an article by its iD.
        put: updates an existing article.
        delete: deletes an article.
    """

    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        """
        Util function to fetch an article.
        Returns an article
        """
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            response = {
                "message": "Article not found."
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
        return article

    def get(self, request, pk):
        """
        Retrieves an article by its ID.
        """
        article = self.get_object(pk=pk)

        serializer = ArticleSerializer(article)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        """
        Updates an existing article.
        Returns an updated article or error.
        """
        article = self.get_object(pk=pk)

        serializer = ArticleSerializer(data=request.data, instance=article)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Deletes an existing article.
        """
        article = self.get_object(pk=pk)

        article.delete()

        response = {
                "message": "Article deleted successfully."
            }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    


class CommentCreateView(APIView):
    """
    Handles adding a comment to an article.
    - POST: Creates a new comment.
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Util function to fetch an article.
        Returns an article
        """
        article = get_object_or_404(Article, id=pk)
        
        return article

    def post(self, request, pk):
        """
        Creates a new comment for an article.
        """
        article = self.get_object(pk=pk)

        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeArticleView(APIView):
    """
    Handles liking an article.
    - POST: Likes an article.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Util function to fetch an article.
        Returns an article
        """
        article = get_object_or_404(Article, id=pk)
        
        return article

    def post(self, request, pk):
        """
        Handles POST request for liking an article.
        """
        article = self.get_object(pk=pk)

        # checks if the user has already liked the article
        if Like.objects.filter(article=article, user=request.user).exists():
            response = {
                "message": "Already liked this article."
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        # creates a like object
        Like.objects.create(article=article, user=request.user)

        response = {
                "message": "Article liked."
            }

        return Response(response, status=status.HTTP_201_CREATED)


class ShareArticleView(APIView):
    """
    Handles sharing an article.
    - POST: Shares an article.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Util function to fetch an article.
        Returns an article
        """
        article = get_object_or_404(Article, id=pk)
        
        return article

    def post(self, request, pk):
        """
        Handles POST request for sharing an article.
        """

        article = self.get_object(pk=pk)
        
        share = Share.objects.create(article=article, user=request.user)
        response = {
                "message": "Article shared successfully."
            }
        return Response(response, status=status.HTTP_201_CREATED)
