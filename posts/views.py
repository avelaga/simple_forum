from django.shortcuts import render
from .models import Post, Comment
from rest_framework import generics
from .serializers import CommentSerializer, PostSerializer

# POSTS 

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

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