from django.contrib import admin
from django.urls import path
from . import views

app_name = 'schedules'
urlpatterns = [
    path('workspace/<int:workspace_pk>/', views.schedule_list, name='schedule_list'),
    path('workspace/<int:workspace_pk>/create/', views.schedule_create, name='schedule_create'),
    path('workspace/<int:workspace_pk>/schedule/<int:schedule_pk>/update/', views.schedule_update, name='schedule_update'),
    path('workspace/<int:workspace_pk>/schedule/<int:schedule_pk>/delete/', views.schedule_delete, name='schedule_delete'),
]
