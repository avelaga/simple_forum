from django.shortcuts import render
from .models import Post, Comment
from rest_framework import generics
from .serializers import CommentSerializer, PostSerializer

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class CommentList(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer