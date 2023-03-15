from django.db import models
from helpApp.models import Subject

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class User_subject(models.Model):
    # auth.user.id, helpApp_subject, can_submit
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    can_submit = models.BooleanField(default=False)