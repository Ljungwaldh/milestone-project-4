from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Profile
from checkout.models import Order
from gameproject.models import GameProject


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)

    orders = Order.objects.filter(user=profile).order_by('-created_at')

    game_projects = GameProject.objects.filter(
                                 owner=profile).order_by('-created_at')

    for game_project in game_projects:
        game_project.total_amount = 0
        for order in Order.objects.filter(
                game_project=game_project).filter(status='PA'):
            game_project.total_amount += order.donation_item.amount

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
        'game_projects': game_projects,
    }

    return render(request, template, context)
