from django.db import models


# Create your models here.
class Board(models.Model):
    # 보드는 수정, 삭제 불가능
    # 추후에 commit=False로 게시글이 생성될 때 db에 따로 저장할 예정
    name = models.CharField(max_length=20)


class Article(models.Model):
    # 우선순위 필드는 게시글 생성폼에서 select 태그의 option을 통해
    # very important, important, normal 이 세 개 중 하나의 데이터를 저장할 예정
    priority = models.TextField()
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 보드를 외래키로
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    # 나머지 외래키는 아직 받지 않은 상태(이메일, 워크스페이스, 카테고리)


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 게시글을 외래키로
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 나머지 외래키는 아직 받지 않은 상태(이메일)


class Image(models.Model):
    # media/images에 이미지 저장
    image = models.ImageField(upload_to="images", null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class File(models.Model):
    # media/files에 파일 저장
    file = models.FileField(upload_to="files", null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
