from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    timestamp = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    liked_users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_users", null=True, default=None)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comments", null=True, default=None)
