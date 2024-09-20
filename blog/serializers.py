from rest_framework import serializers
from .models import Article, Comment, Like, Share

from account.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    Fields:
        id (UUIDField): unique identifier for the comment.
        article(Article): the article commented on.
        user (User): the user commenting on an article.
        comment (TextField): the content of the comment.
        created_date (DateTimeField): timestamp when the comment was made.
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment', 'created_date']

class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Article model.

    Handles serialization and deserialization of Article objects.

    Fields:
        id (UUIDField): unique identifier for the article.
        user (User): the author of the article.
        title (CharField): the article's title.
        tags (CharField): the article's tags.
        body (TextField): the content of the article.
        featured (BooleanField): marks if an article should be viewed by everyone.
        published_date (DateTimeField): timestamp when the article was created.
        updated_date (DateTimeField): timestamp when the article was updated.

    """
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    shares_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField(source='comments.comment')

    user = UserSerializer(read_only=True)
    # user = serializers.CharField(read_only=True, source="user.username") to fetch only the username

    class Meta:
        model = Article
        fields = [
            "id", "user", "title", "tags","body", "featured",'comments_count','likes_count', 'shares_count','comments'
        ]
        read_only_fields = ["id", "user", "published_date", "updated_date"]



    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_shares_count(self, obj):
        return obj.shares.count()
    
    def get_comments(self, obj):
        comments_data = Comment.objects.filter(article=obj)
        comments = CommentSerializer(comments_data, many=True)
        return comments.data


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    Fields:
        id (UUIDField): unique identifier for the comment.
        article(Article): the article commented on.
        user (User): the user commenting on an article.
        comment (TextField): the content of the comment.
        created_date (DateTimeField): timestamp when the comment was made.
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment', 'created_date']


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.

    Fields:
        id (UUIDField): unique identifier for the Like.
        article(Article): the article being liked.
        user (User): the user liking the article.
    """
    class Meta:
        model = Like
        fields = ['id', 'article', 'user']


class ShareSerializer(serializers.ModelSerializer):
    """
    Serializer for the Share model.

    Fields:
        id (UUIDField): unique identifier for the share object.
        article(Article): the article being shared.
        user (User): the user sharing an article.
        shared_date (DateTimeField): timestamp when the article was shared.
    """
    class Meta:
        model = Share
        fields = ['id', 'article', 'user', 'shared_date']
