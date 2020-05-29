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

import json
from django.http import HttpResponse


def client_sent_payment(request):

    pid = request.POST.get('client_secret').split('_secret')[0]
    print(pid)
    order = get_object_or_404(Order, stripe_pid=pid)
    print(order)

    if request.method == 'POST':
        order.status = 'PS'
        print(order)
        order.save()
        return HttpResponse(content='Webhook Received: Payment Sent',
                            status=200)
    else:
        return HttpResponse(content=('Webhook Received: Payment \
                            unsuccessfully sent'),
                            status=400)


@login_required
def donate(request):

    if request.method == 'POST':

        pid = request.POST.get('client_secret').split('_secret')[0]
        order = get_object_or_404(Order, stripe_pid=pid)

        # ATTEMPTED THIS CODE IN VERSION THAT WASN'T WORKING FOR 'POST (PRODUCING BAD REQUESTS)
        # if order.status == 'PE':
        return redirect(reverse('donate_success', args=[order.order_number]))
        # else:
        #     messages.error(request, 'Sorry, your donation was not \
        #     processed successfully.')
        #     return HttpResponse(status=400)

    if request.method == 'GET':

        # Getting data from the client
        donation_type = request.GET.get('donation_type')
        game_project = request.GET.get('game_project')
        donation = get_object_or_404(Donation, pk=donation_type)
        project = get_object_or_404(GameProject, pk=game_project)
        profile = get_object_or_404(Profile, user=request.user)

        if profile == project.owner:
            messages.error(request, 'Sorry, you cannot donate to your own project')
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
            'client_secret': intent.client_secret
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





@csrf_exempt
def stripe_webhook_receiver(request):

  payload = request.body
  event = None


  stripe.api_key = settings.STRIPE_SECRET_KEY

  try:
    event = stripe.Event.construct_from(
      json.loads(payload), stripe.api_key
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)

  # Handle the event
  if event.type == 'payment_intent.succeeded':
    payment_intent = event.data.object # contains a stripe.PaymentIntent
    # Then define and call a method to handle the successful payment intent.
    # handle_payment_intent_succeeded(payment_intent)
  elif event.type == 'payment_method.attached':
    payment_method = event.data.object # contains a stripe.PaymentMethod
    # Then define and call a method to handle the successful attachment of a PaymentMethod.
    # handle_payment_method_attached(payment_method)
  # ... handle other event types
  else:
    # Unexpected event type
    return HttpResponse(status=400)

  return HttpResponse(status=200)


    # CODE THAT WAS WITHIN WEBHOOK FUNCTION PREVIOUSLY :

        # wh_secret = settings.STRIPE_WH_SECRET
        # stripe.api_key = settings.STRIPE_SECRET_KEY

        # # Get the webhook data and verify its signature
        # payload = request.body
        # sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        # event = None

        # print("1")
        # try:
        #     print("2")
        #     event = stripe.Webhook.construct_event(
        #       payload, sig_header, wh_secret
        #     )
        # except ValueError as e:
        #     print("3")
        #     print(e)
        #     # Invalid payload

        #     return HttpResponse(status=400)
        # except stripe.error.SignatureVerificationError as e:
        #     # Invalid signature
        #     print("4")
        #     print(e)
        #     return HttpResponse(status=400)

        # # Handle the event
        # if event.type == 'payment_intent.succeeded':
        #     payment_intent = event.data.object  # contains a stripe.PaymentIntent
        #     print('PaymentIntent was successful!')
        #     order = get_object_or_404(Order, stripe_pid=payment_intent.id)
        #     # print('*** order : ', dir(order))
        #     order.status = 'PA'
        #     order.save()

        # elif event.type == 'payment_intent.payment_failed':
        #     payment_intent = event.data.object
        #     print('PaymentIntent was unsuccessful')
        #     order = get_object_or_404(Order, stripe_pid=payment_intent.id)
        #     order.status = 'FA'
        #     order.save()

        # elif event.type == 'payment_method.attached':
        #     payment_method = event.data.object  # contains a stripe.PaymentMethod
        #     print('PaymentMethod was attached to a Customer!')
        # # ... handle other event types
        # else:
        #     # Unexpected event type
        #     payment_intent = event.data.object
        #     print('Unexpected event type')
        #     order = get_object_or_404(Order, stripe_pid=payment_intent.id)
        #     order.status = 'CA'
        #     order.save()
        #     return HttpResponse(status=400)

        # return HttpResponse(status=200)
