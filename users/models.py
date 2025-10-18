from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    google_id = models.CharField(max_length=225, unique=True, null=True, blank=True)
    email = models.EmailField(blank=True, null=True) 

    def __str__(self):
        return self.username 
