from django.db import models
from django.conf import settings
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

# Create your models here.
# class Workspace(models.Model):
#     name = models.CharField(max_length=20)
#     favorite = models.ManyToManyField('유저', symmetrical = False, related_name='favorite')

# class category(models.Model):
#     name = models.CharField(max_length=20)
#     workspace_id = models.ForeignKey(Workspace, on_delete=models.CASCADE)
