from django import forms
from .models import Article, Comment
from django_summernote.widgets import SummernoteWidget


PRIORITY = [
        ('1', 'π΄'),
        ('2', 'π‘'),
        ('3', 'π’'),
        ]

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'article-title',
                'placeholder': 'μ λͺ©μ μλ ₯νμΈμ.',
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
                'placeholder': 'λκΈμ μλ ₯νμΈμ.',
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ('content',)
