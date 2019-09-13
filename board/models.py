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


"""def total_likes(self):
    return self.likes.count()"""