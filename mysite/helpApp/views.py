from django.http.response import HttpResponse
from django.shortcuts import render

def studyTimetable(request):
    return render(request, 'helpApp/studytimetable.html')

def examTimetable(request):
    return render(request, 'helpApp/examtimetable.html')

def checkSubject(request):
    return render(request, 'helpApp/checksubject.html')
