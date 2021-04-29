from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()

class Comment(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField()
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")