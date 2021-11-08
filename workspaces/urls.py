# from django import urls
from django.urls import path
from . import views

app_name = 'workspaces'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_workspace, name='create_workspace'),
]
