from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username
