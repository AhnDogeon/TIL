from django.urls import path
from . import views

app_name = 'board_ad'

urlpatterns = [
    # Create
    path('new/', views.create_posting, name='new_posting'),

    # Read
    path('', views.posting_list, name='posting_list'),  # DOMAIN/articles
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),  # DOMAIN/articles/1

    # U
    path('<int:posting_id>/update/', views.posting_update, name='posting_update'), # DOMAIN/postings/1/edit

    # D
    path('<int:posting_id>/delete/', views.posting_delete, name='posting_delete'), # DOMAIN/postings/1/delete

    path('<int:posting_id>/comments/create/', views.create_comment, name='create_comment'), # DOMAIN/postings/1/comments/create
    path('<int:posting_id>/comments/<int:comment_id>/delete', views.delete_comment, name='delete_comment'), # /postings/1/comments/1/delete
]