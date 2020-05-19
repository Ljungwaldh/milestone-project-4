from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'donation_item', 'game_project')

    def __init__(self, *args, **kwargs):
        self.fields.widget.attrs['class'] = 'stripe-style-input'
