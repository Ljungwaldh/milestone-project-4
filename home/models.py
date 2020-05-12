from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class SubscriptionPlan (models.Model):
    name = models.CharField(max_length=254)
    reward = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tier = models.ForeignKey(Tier, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tier (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_creator = models.Boolean(default=False, null=True, blank=True)

    def __str__(self):
        return self.user


class GameProject (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(Profile, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=False, null=False, default=timezone.now)

    def __str__(self):
        return self.title


class Comment (models.Model):
    content = models.TextField()
    user = models.ForeignKey(Profile, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=False, null=False, default=timezone.now)
    blog_article = models.ForeignKey(BlogArticle, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class BlogArticle (models.Model):
    blog_title = models.CharField(max_length=50)
    blog_content = models.TextField()
    game_project = models.ForeignKey(GameProject, null=False, blank=False, on_delete=models.CASCADE)
    tiers = models.ForeignKey(Tiers, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=False, null=False, default=timezone.now)

    def __str__(self):
        return self.blog_title


class Order (models.Model):
    user = models.ForeignKey(Profile, null=False, blank=False, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, null=False, blank=False, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32, null=False, editable=False)

    def __str__(self):
        return self.order_number