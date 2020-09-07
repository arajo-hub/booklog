from django.db import models
from booklog import settings

class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    publisher=models.CharField(max_length=255)
    pubdate=models.DateTimeField()
    review=models.TextField(max_length=255)

    def __str__(self):
        return self.title
