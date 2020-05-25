from django import forms
from .models import Profile
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.db import models


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class CustomSignupForm(SignupForm):

    # is_creator = forms.BooleanField(label='is creator', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_creator'] = forms.BooleanField(label='Sign up as a Creator', required=False)

    def save(self, request):
        is_creator = self.cleaned_data.pop('is_creator')

        user = super().save(request)
        if user:
            Profile.objects.create(user=user, is_creator=is_creator)
        return user
