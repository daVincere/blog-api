from rest_framework import serializers 

from post.models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['heading', 'description', 'timestamp', 'photo']

class PostViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['heading', 'description', 'timestamp', 'photo']