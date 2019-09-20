from django.db import models
from django.urls import reverse
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Board_element(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    likes = models.ManyToManyField(User ,related_name='likes',blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title



"""def total_likes(self):
    return self.likes.count()"""
