from rest_framework.generics import ListAPIView, RetrieveAPIView
from post.models import Post
from post.api.serializers import PostSerializer, PostViewSerializer

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostViewSerializer
	lookup_field = 'slug'