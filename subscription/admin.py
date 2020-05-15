from django.contrib import admin

from .models import SubscriptionPlan, Tier

admin.site.register(SubscriptionPlan)
admin.site.register(Tier)
