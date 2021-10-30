from django.db import models

# Create your models here.
class Article(models.Model):
    # 우선순위 필드는 게시글 생성폼에서 select 태그의 option을 통해
    # very important, important, normal 이 세 개 중 하나의 데이터를 저장할 예정
    priority = models.TextField()
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 나머지 외래키는 아직 받지 않은 상태(이메일, 워크스페이스, 보드, 카테고리)