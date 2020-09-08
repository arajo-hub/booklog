from django.db import models
from booklog import settings
from django.contrib.auth import get_user_model

User=get_user_model()

class Post(models.Model):
    user=models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    publisher=models.CharField(max_length=255)
    pubdate=models.DateTimeField()
    review=models.TextField(max_length=255)

    def __str__(self):
        return self.title
