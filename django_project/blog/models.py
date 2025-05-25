from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# This code defines a Django model for a blog post.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # This line creates a foreign key relationship with the User model.
    # The on_delete=models.CASCADE means that if the user is deleted, all their posts will also be deleted.