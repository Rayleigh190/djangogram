from django.db import models
from common.models import User


class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post_author'
    )
    image = models.ImageField()
    caption = models.TextField(blank=True)
    image_likes = models.ManyToManyField(User, blank=True, related_name='post_image_likes')


class Comment(TimeStampedModel):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
