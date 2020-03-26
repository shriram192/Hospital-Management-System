from django.db import models

# Create your models here.

class Type(models.Model):
    username = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    value = models.Manager()
    