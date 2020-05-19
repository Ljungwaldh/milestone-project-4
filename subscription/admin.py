from django.contrib import admin

from .models import SubscriptionPlan, Tier, Donation_Old

admin.site.register(SubscriptionPlan)
admin.site.register(Tier)
admin.site.register(Donation_Old)
