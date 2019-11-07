from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'timestamp']
	class Meta:
		model = Post
		fields = ('id', 'heading')


admin.site.register(Post, PostAdmin)