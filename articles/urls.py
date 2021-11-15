from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('<int:workspace_pk>/workspace/<int:category_pk>/category/', views.index_article, name='index_article'),
    path('<int:workspace_pk>/workspace/<int:category_pk>/category/<int:board_pk>/board/create_article/', views.create_article, name='create_article'),
    path('<int:article_pk>/<int:board_pk>/modify_article_board/', views.modify_article_board, name='modify_article_board'),
    path('<int:article_pk>/detail_article/', views.detail_article, name='detail_article'),
    path('<int:article_pk>/update_article/', views.update_article, name='update_article'),
    path('<int:article_pk>/delete_article/', views.delete_article, name='delete_article'),
    path('<int:article_pk>/article/create_comment/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/article/<int:comment_pk>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('<int:article_pk>/article/<int:image_pk>/delete_image/', views.delete_image, name='delete_image'),
    path('<int:article_pk>/article/<int:file_pk>/delete_file/', views.delete_file, name='delete_file'),
]
