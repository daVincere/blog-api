from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
	path('signup', views.signup, name='signup'),
	path('login', views.login_view, name='login'),
	path('userlist', views.user_list, name='user_list'),
	path('profile', views.self_profile, name='self_profile'),
	path('u/<username>', views.public_profile, name='profile'),
	path('logout', views.logout_view, name='logout_view'),
	]