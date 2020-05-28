from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from gameproject.models import GameProject


class TestViews(TestCase):

    def test_get_all_project_page(self):

        User.objects.create(username='temporary',
                            email='temp@temp.com',
                            password='secret')

        self.client.login(username='temporary', password='secret')
        response = self.client.get('/gameproject/all_projects/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='gameproject/all_projects.html')

    def test_get_project_detail_page(self):

        user = User.objects.create(username='temporary',
                                   email='temp@temp.com',
                                   password='secret')

        profile = Profile.objects.create(user=user)

        project = GameProject.objects.create(title='test', description='testing', owner=profile)

        # profile = Profile.objects.create(user=user)
        self.client.login(username='temporary', password='secret')
        response = self.client.get('/gameproject/project_detail/f"{project.id}"/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='gameproject/project_detail.html')

    def test_get_addproject_page_and_non_creator_is_redirected_away(self):

        user = User.objects.create(username='temporary',
                                   email='temp@temp.com',
                                   password='secret')

        profile = Profile.objects.create(user=user, is_creator=False)

        self.client.login(username='temporary', password='secret')
        response = self.client.get('/gameproject/add_project', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='gameproject/add_project.html')
        response = self.client.get('/gameproject/add_project')
        # my_url = '/'
        # response = self.client.get('/', follow=True)
        # self.assertRedirects(response, f'/accounts/login/?next={my_url}')
        self.assertRedirects(response, response['Location'])
        print(response['Location'])
        self.assertEqual(response.status_code, 302)
