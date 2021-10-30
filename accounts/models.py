from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, primary_key=True)
    image = models.ImageField(upload_to="profile-images", null=True, blank=True)