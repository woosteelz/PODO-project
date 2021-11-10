from django.db import models
from django.conf import settings
from workspaces.models import Workspace
from datetime import time, date, datetime


def default_zero_time():
    return time(0, 0)

class Schedule(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    priority = models.CharField(max_length=50, default='3')
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    start_time = models.TimeField(blank=True, null=True, default=time)
    end_time = models.TimeField(blank=True, null=True, default=time)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    favorite_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_schedules')


    def __str__(self):
        return self.title
