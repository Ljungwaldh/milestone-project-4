from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import Profile
from checkout.models import Order
from gameproject.models import GameProject, Donation


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)

    orders = Order.objects.filter(user=profile).order_by('-created_at')

    game_projects = GameProject.objects.filter(owner=profile).order_by('-created_at')

    project_orders = GameProject.objects.filter(owner=profile).Order_set.all()
    print(project_orders)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
        'game_projects': game_projects,
    }

    return render(request, template, context)
