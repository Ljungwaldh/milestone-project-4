from django import forms
from .models import Profile
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


class UserForm(forms.ModelForm):
    """Form provided by django-allaiuth for user registration"""
    class Meta:
        model = User
        fields = ['username', 'email']


class CustomSignupForm(SignupForm):
    """Custom sign-up form that adds to the UserForm
    an additonal checkbox field so users can choose to
    sign-up as Creator users"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_creator'] = (
            forms.BooleanField(label='Signup as a Creator', required=False))

    def save(self, request):
        is_creator = self.cleaned_data.pop('is_creator')

        user = super().save(request)
        if user:
            Profile.objects.create(user=user, is_creator=is_creator)
        return user
