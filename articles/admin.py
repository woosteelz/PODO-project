from django.contrib import admin
from .models import Board, Article, Comment, Image, File


# Register your models here.
admin.site.register([Article, Board, Comment, Image, File])