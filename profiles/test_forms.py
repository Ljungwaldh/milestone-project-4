from django.test import TestCase
from .forms import CustomSignupForm


class TestCustomSignupFrom(TestCase):

    def test_username_is_required(self):
        form = CustomSignupForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.error.keys())
        self.assertEqual(form.error['username'][0], 'Please fill in this field.')

    def test_email_is_required(self):
        form = CustomSignupForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.error.keys())
        self.assertEqual(form.error['email'][0], 'Please fill in this field.')

    def test_email2_is_required(self):
        form = CustomSignupForm({'email2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email2', form.error.keys())
        self.assertEqual(form.error['email2'][0], 'Please fill in this field.')

    def test_password_is_required(self):
        form = CustomSignupForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.error.keys())
        self.assertEqual(form.error['password1'][0], 'Please fill in this field.')

    def test_iscreator_is_not_required(self):
        form = CustomSignupForm({'email': 'brian@brian.com', 'email2':
                                 'brian@brian.com', 'username': 'the brian', 'password1': 
                                 'hellothistest', 'password2': 'hellothistest'})

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CustomSignupForm()
        self.assertEqual(form.Meta.fields, ['email', 'email2', 'username', 'password1', 'password2', 'is_creator'])
