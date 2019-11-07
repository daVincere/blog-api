from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

def upload_location(instance, filename):
    return "profile/%s/%s" %(instance.user, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    photo  = models.ImageField(upload_to=upload_location,
                            blank=True,
                            null=True,
                            width_field="width_field",
                            height_field="height_field")
    width_field  = models.IntegerField(default=0, null=True)
    height_field = models.IntegerField(default=0, null=True)
    follows = models.ManyToManyField('self', related_name="is_following", symmetrical=False)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"username" : self.user.username})

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()