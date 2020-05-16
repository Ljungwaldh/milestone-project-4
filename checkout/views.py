from django.shortcuts import render, get_object_or_404
from gameproject.models import GameProject
from subscription.models import Donation


def donate(request):

    print(request.GET.get('game_project'))
    donation_type = request.GET.get('donation_type')
    game_project = request.GET.get('game_project')
    project = get_object_or_404(GameProject, pk=game_project)
    donation = get_object_or_404(Donation, pk=donation_type)

    template = 'checkout/checkout.html'
    context = {
        'donation': donation,
        'project': project,
    }

    return render(request, template, context)
