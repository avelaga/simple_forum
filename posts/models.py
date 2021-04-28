from django.db import models
from django.contrib.auth.models import User

# - Post
#   - title
#   - body
#   - [Comments]

# - Comment
#   - User
#   - Post
#   - body

class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  # comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Comment(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField()
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")