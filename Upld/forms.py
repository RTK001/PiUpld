from django import forms
from .git_interface import validate_git_url
from .models import GitHubProject

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = GitHubProject
        fields = ['git_link',]

    def clean_git_link(self):
        data = self.cleaned_data['git_link']
        if validate_git_url(data):
            return data
        else:
            raise forms.ValidationError("Invalid Git repository!", code='invalid')
