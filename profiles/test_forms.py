from django.test import TestCase
from .forms import CustomSignupForm


class TestCustomSignupFrom(TestCase):
    """Testing done to confirm which fields are required/not required"""

    def test_username_is_required(self):
        form = CustomSignupForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_email_is_required(self):
        form = CustomSignupForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_email2_is_required(self):
        form = CustomSignupForm({'email2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email2', form.errors.keys())
        self.assertEqual(form.errors['email2'][0], 'This field is required.')

    def test_password_is_required(self):
        form = CustomSignupForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(
            form.errors['password1'][0], 'This field is required.')

    def test_iscreator_is_not_required(self):
        form = CustomSignupForm({'email': 'brian@brian.com', 'email2':
                                 'brian@brian.com',
                                 'username': 'thebrian',
                                 'password1': 'hellothistest',
                                 'password2': 'hellothistest'})
        self.assertTrue(form.is_valid())
