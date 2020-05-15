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

    print("****")
    print(type(profile))
    print("****")

    orders = Order.objects.filter(user=profile) # Display what user is subscribed to

    print("****")
    print(orders)
    print("****")

    # game_project = orders.subscription_plan.gameproject.all()
    game_project = GameProject.objects.filter(owner=profile) # Displaying, if a creator, what projects they've created + any relevant data

    print("****")
    print(game_project)
    print("****")


    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
        'game_project': game_project,
    }

    return render(request, template, context)
