from django.shortcuts import render
from .models import Post, Comment
from rest_framework import generics, permissions
from .serializers import CommentSerializer, PostListSerializer, PostDetailSerializer
from .permissions import IsOwnerOrReadOnly

# POSTS 

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostListSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  # associate this post with it's user
  def perform_create(self, serializer):
    serializer.save(profile=self.request.user)

class PostDetail(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostDetailSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostDelete(generics.DestroyAPIView):
  queryset = Post.objects.all()

# COMMENTS 

class CommentList(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  # associate this comment with it's user
  def perform_create(self, serializer):
    serializer.save(profile=self.request.user)

class CommentDetail(generics.RetrieveAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentDelete(generics.DestroyAPIView):
  queryset = Comment.objects.all()