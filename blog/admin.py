from django.contrib import admin
from .models import Article, Comment, Like, Share

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Share)
