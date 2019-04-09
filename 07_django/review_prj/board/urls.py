from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), # DOMAIN/board_ad/index
    path('greeting/<str:name>/<str:role>/', views.greeting), # DOMAIN/board_ad/greeting/dg
    # Create
    # /articles/new => html # 새로 작성하는 화면
    path('articles/new/', views.article_new),
    #/articles/create => DB에 new record 작성
    path('articles/create/', views.article_create),

    # Read
    # /articles => html (all articles)
    path('articles/', views.article_list),
    # /articles => html (article id 1)
    path('articles/<int:id>/', views.article_detail),

    # Update
    # /articles/1/edit => html (article id  = 1수정하는 화면)
    path('articles/<int:id>/edit/', views.article_edit),
    # /articles/1/update => DB update article id = 1
    path('articles/<int:id>/update/', views.article_update),

    # Delete
    # /articles/1/delete => DB delete article id = 1
    path('articles/<int:id>/delete/', views.article_delete),

]