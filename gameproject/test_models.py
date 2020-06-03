from django.test import TestCase
from .models import Donation, GameProject


class TestModel(TestCase):
    """Simple tests testing that what is returned from
    a string method is correct"""
    def test_string_is_equal_to_title_for_gameproject(self):
        game_project = GameProject.objects.create(
              title='test', description='testing')
        self.assertEqual(str(game_project), game_project.title)

    def test_string_is_equal_to_title_for_donation(self):
        donation = Donation.objects.create(
            title='test', description='testing', amount=10.00)
        self.assertEqual(str(donation), donation.title)
