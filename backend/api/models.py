from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
import uuid
from datetime import datetime
# Create your models here.

# Step 2 Define models
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    followers = models.BigIntegerField(default=0)
    following = models.BigIntegerField(default=0)
    profileImage = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user