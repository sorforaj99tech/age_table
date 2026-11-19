from django.db import models

# Create your models here.

class Signup(models.Model):
    
    username = models.CharField()
    sub = models.CharField()
    age = models.IntegerField()