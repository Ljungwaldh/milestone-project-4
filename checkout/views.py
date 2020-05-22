from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
from gameproject.models import GameProject, Donation
from profiles.models import Profile
from .models import Order


def client_sent_payment(request):
    if request.method == 'POST':
        print(request.POST.get('message'))
        # change order status to 'payment sent'
        # retrieve order object (filter on id ? client secret ?)
        # order.status = 'PS'
        # order.save()
        return HttpResponse(content='something', status=200)


@login_required
def donate(request):

    if request.method == 'GET':

        # Getting data from the client
        donation_type = request.GET.get('donation_type')
        game_project = request.GET.get('game_project')
        donation = get_object_or_404(Donation, pk=donation_type)
        project = get_object_or_404(GameProject, pk=game_project)

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
            'client_secret': intent.client_secret
        }

        return render(request, template, context)


@login_required
def donate_success(request):
    template = 'checkout/checkout_success.html'
    context = {}
    return render(request, template, context)


@csrf_exempt
def stripe_webhook_receiver(request):

    payload = request.body
    event = None
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object  # contains a stripe.PaymentIntent
        print('PaymentIntent was successful!')
        print(payment_intent)
        order = get_object_or_404(Order, stripe_pid=payment_intent.id)
        # print('*** order : ', dir(order))
        order.status = 'PA'
        order.save()

    elif event.type == 'payment_method.attached':
        payment_method = event.data.object  # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
    # ... handle other event types
    else:
        # Unexpected event type
        return HttpResponse(status=400)

    return HttpResponse(status=200)
