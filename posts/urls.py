from django.urls import path
from . import views, like_views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.post_create, name='post_create'),
    path('modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('<int:post_id>/comment_create/', views.comment_create, name="comment_create"),
    path('<int:comment_id>/comment_delete/', views.comment_delete, name="comment_delete"),
    path('<int:comment_id>/comment_modify/', views.comment_modify, name="comment_modify"),

    # like_views.py
    path('like/post/<int:post_id>/', like_views.like_post, name="like_post"),
    path('like-delete/post/<int:post_id>/', like_views.like_delete, name="like-delete_post"),
]
