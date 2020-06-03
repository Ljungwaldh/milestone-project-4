from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model that stores data from both the UserForm and
    CustomSignUpForm. This model stores instances of profiles"""

    class Meta:
        pass

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.user.username
