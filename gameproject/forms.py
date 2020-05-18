from django import forms
from .models import GameProject


class ProjectForm(forms.ModelForm):

    class Meta:
        model = GameProject
        fields = ('title', 'description', 'owner')
