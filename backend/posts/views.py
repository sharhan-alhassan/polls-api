

from django.db.models import query
from .serializers import PostSerializer, UserSerializer
from .models import Post

from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .permissions import IsAuthorOrReadOnly

from django.contrib.auth import get_user_model
from rest_framework import viewsets

# Create your views here.
'''
class PostList(ListCreateAPIView):
    # ListCreateAPIView creates read-write endpoint 
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    # RetrieveUpdateDestroyAPIView creates read-updated-delete endpoint
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,) # new
'''

'''
class UserList(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
'''

# refactoring with ModelViewSet
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

