from rest_framework import serializers
from .models import Article

from account.serializers import UserSerializer

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

    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            "id", "user", "title", "tags","body", "featured"
        ]
        read_only_fields = ["id", "user", "published_date", "updated_date"]
