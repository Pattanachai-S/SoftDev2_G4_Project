from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)