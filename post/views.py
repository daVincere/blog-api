from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post
from django.contrib import messages
# Create your views here.
@login_required
def post_create(request):
	"""
		This makes sure that the form accpets a POST requests (of some data) or Nothing.
		Without this the form would even accept empty data.
	"""
	form = PostForm(request.POST or None, request.FILES or None)
	if request.POST:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.success(request, "Post created!")
			return HttpResponseRedirect(instance.get_absolute_url())
		else:
			messages.error(request, "Sorry! Something went wrong.", extra_tags="")
	context = {
		'title': "Create Post",
		'form' : form,
	}
	return render(request, 'post/create.html', context)


def post_view(request, slug):
	instance = get_object_or_404(Post, slug=slug)

	context = {
		'instance' : instance	
	}
	return render(request, 'post/view.html', context)