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
        featured (BooleanField): marks if an article should be viewed by everyone.
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
    featured = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    


class Comment(models.Model):
    """
    Comment model to allow users to comment on articles.

    Attributes:
        id (UUIDField): unique identifier for the comment.
        article(Article): the article commented on.
        user (User): the user commenting on an article.
        comment (TextField): the content of the comment.
        created_date (DateTimeField): timestamp when the comment was made.
    """

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['-created_date']

    id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.article}"


class Like(models.Model):
    """
    Like model to allow users to like an article.

    Attributes:
        id (UUIDField): unique identifier for the Like.
        article(Article): the article being liked.
        user (User): the user liking the article.
    """

    class Meta:
        verbose_name_plural = "Likes"
        unique_together = ('article', 'user')  # Ensure a user can like an article only once


    id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey(Article, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} liked {self.article}"


class Share(models.Model):
    """
    Share model to track the sharing of articles by users.

    Attributes:
        id (UUIDField): unique identifier for the share object.
        article(Article): the article being shared.
        user (User): the user sharing an article.
        shared_date (DateTimeField): timestamp when the article was shared.
    """
    class Meta:
        verbose_name_plural = "Shares"
        
    id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey(Article, related_name='shares', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} shared {self.article}"
