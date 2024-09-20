import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    """
    Article model to representing a blog article.

    Attributes:
        id (UUIDField): unique identifier for the article.
        user (User): the author of the article.
        title (CharField): the article's title.
        tags (CharField): the article's tags.
        body (TextField): the content of the article.
        published_date (DateTimeField): timestamp when the article was created.
        updated_date (DateTimeField): timestamp when the article was updated.

    """
    class Meta:
        verbose_name_plural = "Articles"
        ordering = ['-updated_date']

    id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name="articles", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    tags = models.CharField(max_length=250)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
