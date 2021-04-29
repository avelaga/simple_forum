from django.shortcuts import render
from .models import Post, Comment
from rest_framework import generics
from .serializers import CommentSerializer, PostSerializer

class CommentListCreate(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class PostListCreate(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer