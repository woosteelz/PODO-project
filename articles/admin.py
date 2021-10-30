from django.contrib import admin
from .models import Board, Article, Comment, Image, File


# Register your models here.
admin.site.register([Board, Article, Comment, Image, File])