from django.db import models

from django.conf import settings



# Create your models here.

class Schedule(models.Model):
    PRIORITY  = [
        (1, '매우 급함'),
        (2, '급함'),
        (3, '보통'),
        ]

    title = models.CharField(max_length=50)
    content = models.TextField()
    priority = models.IntegerField(choices=PRIORITY, default=3)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(default=0)
    end_time = models.TimeField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)