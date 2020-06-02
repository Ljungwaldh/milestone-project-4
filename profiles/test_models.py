from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


class TestModel(TestCase):
    def test_iscreator_defaults_to_false(self):
        user = User.objects.create(
            email='brian@brian.com',
            username='thebrian',
            password='hellothistest')
        profile = Profile.objects.create(user=user)
        self.assertFalse(profile.is_creator)

    def test_string_is_equal_to_username(self):
        user = User.objects.create(
            email='brian@brian.com',
            username='thebrian',
            password='hellothistest')
        profile = Profile.objects.create(user=user)
        self.assertEqual(str(profile), profile.user.username)
