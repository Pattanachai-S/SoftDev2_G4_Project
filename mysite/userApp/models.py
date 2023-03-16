from django.db import models
from helpApp.models import Subject,Section
from django.contrib.auth.models import User

# Create your models here.
# Use django User Class 


class User_subject(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE,  null=True,blank=True)
    can_submit = models.BooleanField(default=False)
    priority = models.IntegerField(default=10,null=True,blank=True) # priority for add section

    def __str__(self):
        return f"{self.user_id.username} - {self.section.subject_ID.name} Sec{self.section.sec_num}"