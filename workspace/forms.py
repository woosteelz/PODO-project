from django import forms
from django.forms import TextInput
from .models import Workspace

class WorkspaceForm(forms.ModelForm):

    class Meta:
        model = Workspace
        fields = ('image', 'name',)