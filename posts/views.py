from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Comment
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import CommentSerializer
import json

# @csrf_exempt 
# def index(request):
#   p = Post(title="DOGS", body="holy shit thats a lot of dogs on i35")
#   p.save()

#   c1 = Comment(body="comment1", post=p)
#   c2 = Comment(body="comment2", post=p)
#   c3 = Comment(body="comment3", post=p)
#   c1.save()
#   c2.save()
#   c3.save()

#   comments = p.comments.all()

#   print(p)
#   for c in comments:
#     print(c)
#     print(c.body)

#   return HttpResponse("created a post and relevant comment")

# def wrongMethod():
#   response = HttpResponse("Not an available method type")
#   response.status_code = 403
#   return response

# @csrf_exempt 
# def posts(request):
#   if request.method == 'GET':
#     return getPosts(request)
#   elif request.method == 'POST':
#     return newPost(request)
#   return wrongMethod()

# def getPosts(request):
#   posts = Post.objects.all()
#   data = list(posts.values())
#   return JsonResponse(data, safe=False)

# def newPost(request):
#   data = json.loads(request.body)
#   p = Post(title=data['title'], body=data['body'])
#   p.save()
#   return HttpResponse("post " + p.title + " successfully created")

# @csrf_exempt 
# def comments(request):

#   if request.method == 'GET':
#     return getComments(request)
#   elif request.method == 'POST':
#     return newComment(request)
#   return wrongMethod()

# def getComments(request):
#   # need to filter comments by post id
#   comments = Comment.objects.all()
#   data = list(comments.values())
#   return JsonResponse(data, safe=False)

# def newComment(request):
#   requestBody = json.loads(request.body)
#   print(requestBody)
#   if 'post_id' not in requestBody:
#     response = HttpResponse("No post post_id field in request")
#     response.status_code = 403
#     return response
#   p = Post.objects.filter(id=requestBody['post_id'])
#   data = json.loads(requestBody)
#   c = Comment(body=data['body'], post=p)
#   c.save()
#   return HttpResponse("comment " + c.body + " successfully created")

class CommentListCreate(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  # def post(self, request, format=None):
  #   print(request.data)
  #   p = Post.objects.filter(request.body['post_id'])

