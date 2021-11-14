from django import forms
from .models import Article, Comment
from django_summernote.widgets import SummernoteWidget


PRIORITY = [
        ('1', '🔴'),
        ('2', '🟡'),
        ('3', '🟢'),
        ]

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'article-title',
                'placeholder': '제목을 입력하세요.',
            }
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
        fields = ('title', 'content', 'priority',)
        widgets = {
            'content': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):

    content = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'article-comment',
                'placeholder': '댓글을 입력하세요.',
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ('content',)
