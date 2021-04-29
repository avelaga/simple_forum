from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = "__all__"

class PostListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = "__all__"

class PostDetailSerializer(serializers.ModelSerializer):
  comments = CommentSerializer('comments', many=True) # comments reference comes from related_name in model
  class Meta:
    model = Post
    fields = "__all__"