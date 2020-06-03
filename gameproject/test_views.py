from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from gameproject.models import GameProject


class TestViews(TestCase):
    """Two tests that test successful rendering of tow templates
    and the third test testing that users that aren't creators
    are redirected away/restricted from the add_project function
    and template"""
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

        """Instance of project created so that
        there can be a project to access in the test"""
        project = GameProject.objects.create(
            title='test',
            description='testing',
            owner=profile
            )

        self.client.login(username='temporary', password='secret')
        response = self.client.get(
            '/gameproject/project_detail/f"{project.id}"/',
            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            template_name='gameproject/project_detail.html')

    def test_get_addproject_page_and_non_creator_is_redirected_away(self):

        user = User.objects.create(username='temporary',
                                   email='temp@temp.com',
                                   password='secret')

        """Instance of profile created so that
        a profile that isn't a creator is defined"""
        profile = Profile.objects.create(user=user, is_creator=False)

        self.client.login(username='temporary', password='secret')
        response = self.client.get('/gameproject/add_project', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='gameproject/add_project.html')
        response = self.client.get('/gameproject/add_project')
        self.assertRedirects(response, response['Location'])
        self.assertEqual(response.status_code, 302)
