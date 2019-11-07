from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile
		fields = ['user', 'bio', 'photo']

admin.site.register(Profile, ProfileAdmin)