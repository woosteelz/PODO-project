from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
