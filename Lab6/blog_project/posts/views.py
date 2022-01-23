from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

from datetime import datetime
from django.http import HttpResponse


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

def counter(request):
    html = HttpResponse("")
    if request.COOKIES.get('visits'):
        value = int(request.COOKIES.get('visits'))
        html = HttpResponse("<h1>Witaj po raz {}!</h1>".format(value + 1))

        html.set_cookie('visits', value + 1)
    else:
        value = 1
        html = HttpResponse("<h1>Hej nieznajomy!</h1>")
        html.set_cookie('visits', value)
    return html
