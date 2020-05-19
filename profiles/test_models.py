from django.test import TestCase
from .models import Profile


class TestCustomSignupFrom(TestCase):
    def test_iscreator_defaults_to_false(self):
        profile = Profile.objects.create(email='brian@brian.com', username='thebrian', password1='hellothistest', password2='hellothistest')
        self.assertFalse(profile.is_creator)

    def test_string_is_equal_to_username(self):
        profile = Profile.objects.get(pk=1)
        self.assertEqual(str(profile), profile.username)
