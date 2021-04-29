from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import ProfileSerializer

# TODO: how do i make posts and comments field optional in post call to create profile?
class ProfileList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = ProfileSerializer