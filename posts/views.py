from django.shortcuts import render
from .models import Post, Comment
from rest_framework import generics
from .serializers import CommentSerializer, PostListSerializer, PostDetailSerializer

# POSTS 

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostListSerializer

class PostDetail(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostDetailSerializer

class PostDelete(generics.DestroyAPIView):
  queryset = Post.objects.all()

# COMMENTS 

class CommentList(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class CommentDelete(generics.DestroyAPIView):
  queryset = Comment.objects.all()