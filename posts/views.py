from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment

def index(request):
  p = Post(title="DOGS", body="holy shit thats a lot of dogs on i35")
  p.save()

  c1 = Comment(body="comment1", post=p)
  c2 = Comment(body="comment2", post=p)
  c3 = Comment(body="comment3", post=p)
  c1.save()
  c2.save()
  c3.save()
  comments = p.comments.all()
  print(p)
  for c in comments:
    print(c)
    print(c.body)

  return HttpResponse("created a post and relevant comment")