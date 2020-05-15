from django.shortcuts import render, get_object_or_404
from subscription.models import Tier



def subscribe(request, tier_id):
    tier = get_object_or_404(Tier, pk=tier_id)

    subscription = get_object_or_404(tier, pk=subscription_id)
