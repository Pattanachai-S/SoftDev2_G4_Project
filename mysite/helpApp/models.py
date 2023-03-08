from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_ID = models.IntegerField()
    name = models.CharField(max_length=200)
    mid_term = models.DateTimeField('mid term')
    final = models.DateTimeField('final')

class Section(models.Model):
    subject_ID = models.ForeignKey(Subject, on_delete=models.CASCADE)
    sec_num = models.IntegerField()
    day = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
