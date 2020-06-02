from django.test import TestCase
from .forms import ProjectForm
from profiles.models import Profile
from django.contrib.auth.models import User


class TestProjectForm(TestCase):

    def test_title_field_is_required(self):
        form = ProjectForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_description_field_is_required(self):
        form = ProjectForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0],
            'This field is required.'
            )

    def test_valid_form_leads_to_correct_redirect(self):
        user = User.objects.create(username='testuser')
        user.set_password('try12345')
        user.save()
        Profile.objects.create(user=user, is_creator=True)
        self.client.login(username='testuser', password='try12345')

        form = ProjectForm({'title': 'test', 'description': 'testing'})
        post_data = {'title': 'test', 'description': 'testing'}

        response = self.client.post('/gameproject/add_project', post_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(response.status_code, 302)
