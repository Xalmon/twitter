from uuid import uuid4

from django.db import models
from django.conf import settings

# Create your models here.


class Tweet(models.Model):
    text = models.CharField(max_length=200)
    last_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-last_update']


class Comments(models.Model):
    comment = models.CharField(max_length=100)
    commented_on = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

