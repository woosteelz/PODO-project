from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Workspace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    # favorite_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_workspaces')
    image = models.ImageField(default='podoboy.png')
    image_thumbnail = ImageSpecField(
        source='image', processors=[ResizeToFill(45, 45)])
        
        
class Category(models.Model):
    name = models.CharField(max_length=20)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
