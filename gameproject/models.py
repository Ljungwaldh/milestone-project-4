from django.db import models
from django.utils import timezone
from profiles.models import Profile


class GameProject (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(Profile, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=False, null=False, default=timezone.now)

    def __str__(self):
        return self.title
