from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_ID = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mid_term = models.CharField(max_length=200, null=True,blank=True)
    final = models.CharField(max_length=200, null=True,blank=True)
    
    def __str__(self):
        return self.name

class Section(models.Model):
    subject_ID = models.ForeignKey(Subject, on_delete=models.CASCADE)
    sec_num = models.IntegerField()
    day = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.subject_ID.name} - Section {self.sec_num}"
