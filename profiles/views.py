from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from checkout.models import Order
from gameproject.models import GameProject


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)
    subscriptions = profile.orders.all()
    game_project = profile.orders.subscription_plan.gameproject.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'subscriptions': subscriptions,
        'game_project': game_project,
    }

    return render(request, template, context)
