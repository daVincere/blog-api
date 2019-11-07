from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from accounts.forms import SignUpForm
from .models import Profile 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('/')
			else:
				messages.error(request, "Invalid username or password.")
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form':form})

@login_required
def logout_view(request):
	logout(request)
	return redirect('main:index')

@login_required
def user_list(request):
	querylist = Profile.objects.all()
	return render(request, 'accounts/user_list.html', {'querylist': querylist})

# User's Public Profile
@login_required
def public_profile(request, username):
	instance = get_object_or_404(Profile, user__username=username)

	context = {
		"instance" : instance,
	}

	return render(request, 'accounts/public_profile.html', context)

# User's own profile
@login_required
def self_profile(request):
	instance = get_object_or_404(Profile, user=request.user)

	context = {
		"instance" : instance,
	}

	return render(request, 'accounts/self_profile.html', context)


def follow(request):
	return redirect('accounts:user_list')

def unfollow(request):
	return redirect('accounts:user_list')