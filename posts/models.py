from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  profile = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, default=1)
  title = models.CharField(max_length=200)
  body = models.TextField()

class Comment(models.Model):
  profile = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE, default=1)
  body = models.TextField()
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")