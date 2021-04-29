from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post, Comment

class ProfileSerializer(serializers.ModelSerializer):
  posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
  comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name','posts', 'comments']