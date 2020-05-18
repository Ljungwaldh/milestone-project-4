from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from gameproject.models import GameProject
from subscription.models import Donation
from profiles.models import Profile
from checkout.forms import OrderForm
from django.contrib.auth.decorators import login_required


@login_required
def donate(request):

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

    if request.method == 'POST':

        user = get_object_or_404(Profile, user=request.user)
        donation_item = request.POST.get('donation_item')
        game_project = request.POST.get('game_project')

        form_data = {
            'user': user,
            'donation_item': donation_item,
            'game_project': game_project,
        }
        order_form = OrderForm(form_data)
