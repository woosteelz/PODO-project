from django import forms
from .models import Workspace,Category


class WorkspaceForm(forms.ModelForm):

    class Meta:
        model = Workspace
        fields = ('image','name',)


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)