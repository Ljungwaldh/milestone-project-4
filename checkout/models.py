from django.db import models
from subscription.models import SubscriptionPlan
from profiles.models import Profile
from django.utils import timezone


class Order (models.Model):
    user = models.ForeignKey(Profile, null=False, blank=False, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, null=False, blank=False, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    created_at = models.DateTimeField(blank=False, null=False, default=timezone.now)

    def __str__(self):
        return self.order_number
