from django.shortcuts import render
from post.models import Post

# Create your views here.
def error400(request, exception):
    template = 'errors/error.html'
    context = {}
    return render(request, template, status=400)


def error403(request, exception):
    template = 'errors/error.html'
    context = {}
    return render(request, template, status=403)


def error404(request, exception):
    template = 'errors/error.html'
    context = {}
    return render(request, template, status=404)


def error500(request):
    template = 'errors/error.html'
    context = {}
    return render(request, template, status=500)