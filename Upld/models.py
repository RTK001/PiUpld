from django.db import models
from datetime import datetime

class project(models.Model):
    uploaded = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
