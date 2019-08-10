from django.db import models
from django.urls import reverse
from django.conf import settings

from os.path import join
from .git_interface import clone_repo, delete_project
from .managers import BulkQueryManager


UPLOADS_PATH = join(settings.MEDIA_ROOT, "uploads")

class GitHubProject(models.Model):
    uploaded = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    git_link = models.URLField(max_length = 300)
    name = models.SlugField(max_length = 100)
    local_git_repo = models.FilePathField(allow_folders=True, default=UPLOADS_PATH)

    objects = BulkQueryManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.name = self.git_link.split("/")[-1].split(".")[0]
            self.local_git_repo = join( UPLOADS_PATH, self.name)
            git_hub_repo = clone_repo(self.git_link, self.local_git_repo)
        print(self.local_git_repo)
        super(GitHubProject, self).save(*args, **kwargs)
        print(self.local_git_repo)


    def delete(self):
        delete_project(self.local_git_repo)
        super().delete()
