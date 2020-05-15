from django.db import models
from gameproject.models import GameProject


class Tier(models.Model):
    name = models.CharField(max_length=50)
    stripe_subscription_id = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.name


class SubscriptionPlan(models.Model):
    title = models.CharField(max_length=50)
    reward = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    game_project = models.ForeignKey(GameProject, null=False, blank=False, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Donation(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    game_project = models.ForeignKey(GameProject, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
