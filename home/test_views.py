from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class TestViews(TestCase):

    def test_get_home_page(self):

        user = User.objects.create(username='testuser')
        user.set_password('try12345')
        user.save()
        Profile.objects.create(user=user)
        self.client.login(username='testuser', password='try12345')

        self.client.login(username='testuser', password='try12345')
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='home/index.html')
