from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('update/', views.update, name='update'),
    path('delete_image', views.delete_image, name='delete_image'),
    path('delete/', views.delete, name='delete'),
    path('logout/', views.logout, name='logout'),
    path('password/change/', views.password_change, name='password_change'),
    path('invitations/send-invite/', views.invitations_send_invite, name='invitations_send_invite'),
    path('invitations/member/<int:workspace_pk>/', views.invitations_member, name='invitations_member'),
]
