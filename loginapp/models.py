import email
from pyexpat import model
from django.db import models

class user(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)
# Create your models here.
