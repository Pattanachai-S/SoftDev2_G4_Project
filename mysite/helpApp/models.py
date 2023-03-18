from django.db import models
from datetime import datetime

# Create your models here.
class Subject(models.Model):
    subject_ID = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mid_term = models.CharField(max_length=200, null=True,blank=True)
    final = models.CharField(max_length=200, null=True,blank=True)
    mid_term_date = models.CharField(max_length=200, null=True,blank=True)
    mid_term_start_time = models.CharField(max_length=200, null=True,blank=True)
    mid_term_end_time = models.CharField(max_length=200, null=True,blank=True)
    final_term_date = models.CharField(max_length=200, null=True,blank=True)
    final_term_start_time = models.CharField(max_length=200, null=True,blank=True)
    final_term_end_time = models.CharField(max_length=200, null=True,blank=True)
    def __str__(self):
        return self.name

class Section(models.Model):
    subject_ID = models.ForeignKey(Subject, on_delete=models.CASCADE)
    sec_num = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200, null=True,blank=True)
    end_time = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return f"{self.subject_ID.name} - Section {self.sec_num}"
    
    def duration(self):
        start = datetime.strptime(self.start_time, '%H:%M')
        end = datetime.strptime(self.end_time, '%H:%M')
        duration = (end - start).total_seconds() / 3600  # duration in hours
        return duration
