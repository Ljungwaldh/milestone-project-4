from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path(
        'donate_success/<order_number>',
        views.donate_success,
        name='donate_success'),
]
