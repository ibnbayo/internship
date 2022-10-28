from django.db import models

# Create your models here.

class Bio(models.Model):
    slackUsername = models.CharField(max_length = 200)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField(max_length=1000)
    