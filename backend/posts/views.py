

from .serializers import PostSerializer
from .models import Post

from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .permissions import IsAuthorOrReadOnly

# Create your views here.

class PostList(ListCreateAPIView):
    # ListCreateAPIView creates read-write endpoint 
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    # RetrieveUpdateDestroyAPIView creates read-updated-delete endpoint
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,) # new
