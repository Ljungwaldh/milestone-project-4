from django.db import models
from gameproject.models import GameProject
from subscription.models import Tier
from django.utils import timezone


class BlogArticle (models.Model):
    blog_title = models.CharField(max_length=50)
    blog_content = models.TextField()
    game_project = models.ForeignKey(GameProject, null=False, blank=False, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=False, null=False, default=timezone.now)

    def __str__(self):
        return self.blog_title


class Comment (models.Model):
    content = models.TextField()
    user = models.ForeignKey(Profile, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=False, null=False, default=timezone.now)
    blog_article = models.ForeignKey(BlogArticle, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
