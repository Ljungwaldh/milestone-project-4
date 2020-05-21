import uuid
from django.db import models
from profiles.models import Profile
from django.utils import timezone
from gameproject.models import GameProject, Donation


class Order(models.Model):

    STATUS = [
        ('PE', 'Pending'),
        ('SP', 'Send Payment'),
        ('PA', 'Paid'),
        ('CA', 'Cancelled'),
    ]

    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='donations')
    donation_item = models.ForeignKey(Donation, null=True, blank=True, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    created_at = models.DateTimeField(blank=False, null=False, default=timezone.now)
    game_project = models.ForeignKey(GameProject, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS, default='PE')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        Credits to Boutique Ado project by Chris Zielinski.
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        Credits to Boutique Ado project by Chris Zielinski.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.stripe_pid
