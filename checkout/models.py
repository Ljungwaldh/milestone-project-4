from django.db import models
from subscription.models import SubscriptionPlan
from profiles.models import Profile
from subscription.models import Donation
from django.utils import timezone
from gameproject.models import GameProject


# class Order(models.Model):
#     user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='orders')
#     subscription_plan = models.ForeignKey(SubscriptionPlan, null=False, blank=False, on_delete=models.CASCADE)
#     order_number = models.CharField(max_length=32, null=False, editable=False)
#     stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
#     created_at = models.DateTimeField(blank=False, null=False, default=timezone.now)

#     def __str__(self):
#         return self.order_number


class Order(models.Model):
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='donations')
    donation_item = models.ForeignKey(Donation, null=True, blank=True, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    created_at = models.DateTimeField(blank=False, null=False, default=timezone.now)
    game_project = models.ForeignKey(GameProject, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.stripe_pid