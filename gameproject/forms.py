from django import forms
from .models import GameProject


class ProjectForm(forms.ModelForm):

    class Meta:
        model = GameProject
        fields = ('title', 'description', 'image')

    image = forms.ImageField(label='Upload a Cover Image/Photo (Optional)', required=False)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Give your project a gripping title',
            'description': 'Describe what it is all about - get readers/donars excited!',
            'image': 'Upload a Cover Image/Photo (Optional)',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        if field != 'image':
            self.fields[field].label = False
