from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('profiles.urls')),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
]
