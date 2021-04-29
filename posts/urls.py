from django.urls import path

from . import views

urlpatterns = [
  path('comments', views.CommentListCreate.as_view(), name="comment-list-create"),
    path('posts', views.PostListCreate.as_view(), name="post-list-create")
]