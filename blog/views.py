
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsOwner

class ArticleListAPIView(APIView):
    """
    Handles retrieving a list of all articles that are featured.

    Users must be authenticated.

    Methods:
        get: fetches a list of all articles.
    """

    permission_classes = [IsAuthenticated]


    def get(self, request):
        """
        Retrieves all the articles that are featured.
        """
        articles = Article.objects.filter(featured=True)

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