from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from gameproject.models import GameProject, Donation
from profiles.models import Profile
from .models import Order


@login_required
def donate(request):

    if request.method == 'POST':

        pid = request.POST.get('client_secret').split('_secret')[0]
        order = get_object_or_404(Order, stripe_pid=pid)

        order.stripe_pid = pid
        order.status = 'PA'
        order.save()
        return redirect(reverse('donate_success', args=[order.order_number]))

    if request.method == 'GET':

        # Getting data from the client
        donation_type = request.GET.get('donation_type')
        game_project = request.GET.get('game_project')
        donation = get_object_or_404(Donation, pk=donation_type)
        project = get_object_or_404(GameProject, pk=game_project)
        profile = get_object_or_404(Profile, user=request.user)

        if profile == project.owner:
            messages.error(
                request,
                'Sorry, you cannot donate to your own project'
                )
            return redirect(reverse('all_projects'))

        # Create Stripe Payment Intent
        stripe.api_key = settings.STRIPE_SECRET_KEY
        amount = int(donation.amount*100)
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='eur',
            # Verify your integration in this guide by including this parameter
            metadata={'integration_check': 'accept_a_payment'},
        )

        # Creating an order (status: "pending")
        profile = get_object_or_404(Profile, user=request.user)
        donation_type = request.GET.get('donation_type')
        donation_item = get_object_or_404(Donation, pk=donation_type)
        game_project_id = request.GET.get('game_project')
        game_project = get_object_or_404(GameProject, pk=game_project_id)

        order = Order.objects.create(
            user=profile,
            donation_item=donation_item,
            stripe_pid=intent.id,
            game_project=game_project,
            status='PE'
        )
        order.save()

        template = 'checkout/checkout.html'
        context = {
            'donation': donation,
            'project': project,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


@login_required
def donate_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order
    }
    return render(request, template, context)
