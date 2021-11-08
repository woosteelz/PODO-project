from django.db import models 
from django.conf import settings
from workspaces.models import Workspace, Category


# Create your models here.

class Board(models.Model):
    # 보드는 수정, 삭제 불가능
    # 추후에 commit=False로 게시글이 생성될 때 db에 따로 저장할 예정
    name = models.CharField(max_length=20)


class Article(models.Model):
    priority = models.CharField(max_length=10, default='3')
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    favorite_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_articles')


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Image(models.Model):
    # media/images에 이미지 저장
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class File(models.Model):
    # media/files에 파일 저장
    file = models.FileField(upload_to="files/", null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
