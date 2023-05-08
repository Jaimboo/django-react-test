from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return f'{self.user} {self.id}'