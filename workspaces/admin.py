from django.contrib import admin
from .models import Workspace, Category

# Register your models here.
admin.site.register([Workspace, Category])

