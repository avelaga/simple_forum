from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Comment
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
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

@csrf_exempt 
def posts(request):
  if request.method == 'GET':
    return getPosts(request)
  elif request.method == 'POST':
    return newPost(request)
  response = HttpResponse("Not an available method type")
  response.status_code = 403
  return response

def getPosts(request):
  posts = Post.objects.all()
  data = list(posts.values())
  return JsonResponse(data, safe=False)

def newPost(request):
  return HttpResponse("make new post with " + str(request.body))