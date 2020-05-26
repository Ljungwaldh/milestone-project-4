from django import forms
from .models import GameProject


class ProjectForm(forms.ModelForm):

    class Meta:
        model = GameProject
        fields = ('title', 'description', 'owner', 'image')

    image = forms.ImageField(label='Image', required=False)
    title = forms.CharField(label='Title')
    description = forms.CharField(widget=forms.Textarea, label='Description')
