from django.db import models
from django.urls import reverse

from datetime import datetime

class GitHubProject(models.Model):
    uploaded = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    git_link = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
