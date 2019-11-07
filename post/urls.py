from django.urls import path
from . import views

app_name="post"

urlpatterns = [
	path('', views.index, name="index"),
	path('create/', views.post_create, name="create"),
    path('<slug:slug>/', views.post_view, name="post_view"),
]
