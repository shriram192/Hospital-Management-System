from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Doctor(models.Model):
     name = models.CharField(max_length=200)
     did = models.AutoField(primary_key=True)
     value = models.Manager()

class Patient(models.Model):
    name = models.CharField(max_length=200)
    bg= models.CharField(max_length=200)
    age=models.IntegerField()
    pid = models.AutoField(primary_key=True)
    desc=models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    value = models.Manager()