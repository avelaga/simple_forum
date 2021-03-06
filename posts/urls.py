from django.urls import path
from . import views

urlpatterns = [
  path('posts', views.PostList.as_view(), name="post-list"),
  path('posts/<int:pk>', views.PostDetail.as_view(), name="post-detail"),
  path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post-delete"),
  path('comments', views.CommentList.as_view(), name="comment-list"),
  path('comments/<int:pk>', views.CommentDetail.as_view(), name="comment-detail"),
  path('comments/<int:pk>/delete', views.CommentDelete.as_view(), name="comment-delete")
]