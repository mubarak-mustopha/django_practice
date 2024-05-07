from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    slug = models.SlugField(unique=True, max_length=50)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    tags = TaggableManager()

    def __str__(self) -> str:
        return self.title


# many_to_many
# https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_many/
