from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from accounts.forms import SignUpForm, ProfileForm
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
	instance = get_object_or_404(Profile, user__username=request.user.username)
	
	context = {
		"instance" : instance,
	}

	return render(request, 'accounts/self_profile.html', context)

@login_required
def update_profile(request):
	"""
		Updates the user profile
	"""
	instance = get_object_or_404(Profile, user__username=request.user.username)

	form = ProfileForm(request.POST or None, request.FILES or None, instance=instance)
	
	if request.POST:		
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request,"Edited nicely!")
			return HttpResponseRedirect(instance.get_absolute_url())
		else:
			messages.error(request, "Sorry! Unable to Register Updates.", extra_tags="")
	
	context = {
		"instance" : instance,
	}
	
	return render(request, 'accounts/update_profile.html', context)



def follow(request, username):
	user_origin = Profile.objects.get(user__username=username)
	user_profile = Profile.objects.get(user__username=request.user.username)
	
	if user_origin in user_profile.following.all():
		user_profile.following.remove(user_origin)
	else:
		user_profile.following.add(user_origin)
	return redirect('main:index')
