from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
  class meta:
    model = Comment
    fields = "__all__"