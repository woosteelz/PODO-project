# from django import urls
from django.urls import path
from . import views


app_name = 'workspaces'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_workspace, name='create_workspace'),
    path('<int:workspace_pk>/delete/', views.delete_workspace, name='delete_workspace'),
    path('<int:workspace_pk>/category/', views.index_category, name='index_category'),
    path('<int:workspace_pk>/category/create/', views.create_category, name='create_category'),
    path('<int:workspace_pk>/<int:category_pk>/delete/', views.delete_category, name='delete_category'),
    path('<int:workspace_pk>/search/', views.search, name='search'),
]
