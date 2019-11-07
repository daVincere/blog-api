from django.urls import path
from .views import PostListAPIView, PostAPIView

app_name="post"

urlpatterns = [
	path('', PostListAPIView.as_view(), name="api-create"),
    path('<slug:slug>/', PostAPIView.as_view(), name="api-postview"),
]
