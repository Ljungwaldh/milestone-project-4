from django.db import models

# Create your models here.


class Subscriptions (models.Model):
    name = models.Charfield(max_length=254)
    reward = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
