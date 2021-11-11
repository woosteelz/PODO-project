from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('logout/', views.logout, name='logout'),
    path('password/change/', views.password_change, name='password_change'),
]
