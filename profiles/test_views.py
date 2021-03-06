from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    """One test for the profile page rendering successfully with
    a status code of 200"""

    def test_get_profile_page(self):

        User.objects.create(username='temporary',
                            email='temp@temp.com',
                            password='secret')

        self.client.login(username='temporary', password='secret')
        response = self.client.get('/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='profiles/profile.html')
