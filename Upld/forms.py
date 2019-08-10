from django import forms
from .models import GitHubProject

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = GitHubProject
        fields = ['name', 'git_link',]
