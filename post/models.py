from django.db import models
from django.conf import settings
from django.urls import reverse
#for slug field
from django.db.models.signals import pre_save
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

from django.utils import timezone

# class PostManager(models.Manager):
#     def active(self, *args, **kwargs):
#         return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

#     def draft(self, *args, **kwargs):
#         return super(PostManager, self).filter(draft=True)


def upload_location(instance, filename):
    return "post/%s/%s" %(instance.slug, filename)


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    photo  = models.ImageField(upload_to=upload_location,
                            blank=True,
                            null=True,
                            width_field="width_field",
                            height_field="height_field")
    width_field  = models.IntegerField(default=0, null=True)
    height_field = models.IntegerField(default=0, null=True)

    # draft        = models.BooleanField(default=False)
    # publish_time = models.DateTimeField(auto_now=True)
    # last_updated = models.DateTimeField(auto_now=True)
    # objects = PostManager()

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse("posts:post_view", kwargs={"slug" : self.slug})

    class Meta:
        ordering = ["-timestamp"]

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type



def create_slug(instance, new_slug=None):
    slug = slugify(instance.heading)

    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

# signal receiver
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
