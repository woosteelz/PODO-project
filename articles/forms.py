from django import forms
from .models import Article, Comment
from django_summernote.widgets import SummernoteWidget
from django.core.exceptions import ValidationError


# def file_size(value):
#     limit = 2 * 1024 * 1024
#     if value.size > limit:
#         raise ValidationError('File too large. Size should not exceed 2 MiB.')


PRIORITY = [
        ('1', '매우 중요'),
        ('2', '중요'),
        ('3', '보통'),
        ]

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'article-title',
                'placeholder': '  제목을 입력하세요.',
            }
        ),
    )

    content = forms.CharField(
        label='',
        widget=SummernoteWidget(
            attrs={}
        ),
    )

    priority = forms.CharField(
        label='',
        widget=forms.RadioSelect(
            choices=PRIORITY,
            attrs={
                'class': 'article-priority',
            }
        ),
    )

    class Meta:
        model = Article
        fields = ('priority', 'title', 'content', 'priority',)


class CommentForm(forms.ModelForm):

    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'class': 'article-comment',
                'placeholder': '  댓글을 입력하세요.',
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ('content',)
