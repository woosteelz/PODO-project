from django.db import models
from django.conf import settings
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Workspace(models.Model):
    name = models.CharField(max_length=20)
    favorite = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical = False, related_name='favorite')

class Category(models.Model):
    name = models.CharField(max_length=20)
    workspace_id = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    image = models.ImageField(default='podoboy.png')
    image_thumbnail = ImageSpecField(
        source='image', processors=[ResizeToFill(45, 45)])