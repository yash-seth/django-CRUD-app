from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    username = models.CharField(max_length=200,blank=False, default='')
    age = models.IntegerField(max_length=3,blank=False,default=0)
    dob = models.CharField(max_length=10,blank=False,default='')