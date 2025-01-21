from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(
        verbose_name="Birthday",
        null=True
    )
    followers = models.BigIntegerField(default=0)
    following = models.BigIntegerField(default=0)
    posts = models.BigIntegerField(default=0)
    likes = models.BigIntegerField(default=0)

    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    likes = models.BigIntegerField(default=0)
    comments = models.BigIntegerField(default=0)
    link = models.TextField(max_length=255, default=None)
    title = models.CharField(max_length=70, null=False)
    text = models.TextField(max_length=255, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.BigIntegerField(default=0)
    comments = models.BigIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)