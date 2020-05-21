from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('client-sent-payment-to-stripe', views.client_sent_payment, name='client-paying'),
    path('donate_success', views.donate_success, name='donate_success'),
    path('stripe_webhook', views.stripe_webhook_receiver, name='stripe_webhook'),
]
