from django.urls import path
from . import views


app_name = 'schedules'
urlpatterns = [
    path('workspace/<int:workspace_pk>/', views.index, name='index'),
    path('workspace/<int:workspace_pk>/left_month/', views.left_month, name='left_month'),
    path('workspace/<int:workspace_pk>/right_month/', views.right_month, name='right_month'),
    path('workspace/<int:workspace_pk>/create/', views.create_schedule, name='create_schedule'),
    path('workspace/<int:workspace_pk>/schedule/<int:schedule_pk>/update/', views.update_schedule, name='update_schedule'),
    path('workspace/<int:workspace_pk>/schedule/<int:schedule_pk>/delete/', views.delete_schedule, name='delete_schedule'),
]
