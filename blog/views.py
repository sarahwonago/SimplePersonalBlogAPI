
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsOwnerAndAuthenticated


class ArticleListCreateAPIView(APIView):
    """
    Handles retrieving a list of articles and creating new articles.

    Users must be authenticated.

    Methods:
        get: fetches a list of all articles for a specific user.
        post: creates a new article.
    """

    permission_classes = [IsAuthenticated, IsOwnerAndAuthenticated]


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


