from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

def upload_location(instance, filename):
    return "profile/%s/%s" %(instance.user, filename)

class ProfileManager(models.Model):
    use_for_related_fields = True

    def all(self):
        queryset = self.get_queryset().all()
        try:
            if self.instance:
                queryset = queryset.exclude(user=self.instance)
        except:
            pass
        return queryset


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=500, blank=True)
    photo  = models.ImageField(upload_to=upload_location,
                            blank=True,
                            null=True,
                            width_field="width_field",
                            height_field="height_field")
    width_field  = models.IntegerField(default=0, null=True)
    height_field = models.IntegerField(default=0, null=True)
    following = models.ManyToManyField('self', blank=True, related_name="followed_by", symmetrical=False)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"username" : self.user.username})

    def get_following(self):
        """
            Get the users following the current user
        """
        users = self.following.all()
        return users.exclude(user__username=self.user.username)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# class Follower(models.Model):
#     users = models.ManyToManyField(User)
#     user_origin = models.ForeignKey(User, related_name="rel_from_set", null=True, on_delete=models.CASCADE)
#     # user_sink = models.ForeignKey(User, related_name="rel_to_set")
#     # created = models.DateTimeField(auto_add_now=True, db_index=True)

#     @classmethod
#     def add_follower(cls, user_origin, new_follower):
#         follower, created = cls.objects.get_or_create(user_origin=user_origin)

#         follower.users.add(new_follower)

#     @classmethod
#     def lose_follower(cls, user_origin, new_follower):
#         follower, created = cls.objects.get_or_create(user_origin=user_origin)

#         follower.users.remove(new_follower)
