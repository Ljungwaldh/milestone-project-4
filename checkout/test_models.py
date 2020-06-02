from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User
from .models import Order
from gameproject.models import GameProject, Donation


class TestModel(TestCase):
    def test_order_model_string_method_returns_stripe_pid(self):
        user = User.objects.create(
            email='brian@brian.com',
            username='thebrian',
            password='hellothistest'
            )
        profile = Profile.objects.create(user=user)
        game_project = GameProject.objects.create(
            title='test',
            description='testing',
            owner=profile
            )
        donation_item = Donation.objects.create(
            title='test',
            description='test',
            amount=10.00,
            game_project=game_project
            )
        order = Order.objects.create(
            user=profile,
            donation_item=donation_item,
            stripe_pid='12345'
            )
        self.assertEqual(str(order), order.stripe_pid)
