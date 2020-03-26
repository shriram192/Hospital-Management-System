from django.db import models

# Create your models here.
class Node(models.Model):
	nid=models.AutoField(primary_key=True)
	name=models.CharField(max_length=200)
	mc=models.CharField(max_length=200)
	isActive=models.BooleanField(default=False)
	s1=models.CharField(max_length=200)
	s2=models.CharField(max_length=200)
	s3=models.CharField(max_length=200)
	s4=models.CharField(max_length=200)
	s5=models.CharField(max_length=200)
	value = models.Manager()


