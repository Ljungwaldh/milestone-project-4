from django.db import models
from django.utils import timezone
from profiles.models import Profile


class GameProject(models.Model):

    class Meta:
        pass

    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(
        Profile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    created_at = models.DateTimeField(
        blank=False,
        null=False,
        default=timezone.now
        )
    """The Developer has chosen to maek it optional
    to upload images, hence null and black are both set to True"""
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Donation(models.Model):

    class Meta:
        pass

    title = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    game_project = models.ForeignKey(
        GameProject,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.title
