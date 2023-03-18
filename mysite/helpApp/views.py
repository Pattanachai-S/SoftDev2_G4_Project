from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Section, Subject
from userApp.models import User_subject
from django.db.models import Q

def studyTimetable(request):
    course = User_subject.objects.all()
    hour = list(range(8, 21))
    return render(request, 'helpApp/studytimetable.html', {'course':course, 'hour':hour})

def examTimetable(request):
    course = User_subject.objects.all()
    return render(request, 'helpApp/examtimetable.html', {'course':course})

def checkSubject(request):
    if 'search-subject' in request.GET:
        q = request.GET.get('search-subject')
        #subject = Subject.objects.filter(subject_ID__icontains=q)
        multi_q = Q(Q(subject_ID__icontains=q) | Q(name__icontains=q))
        subject = Subject.objects.filter(multi_q)
    else:
        subject = Subject.objects.all()
    context = {'subject':subject}
    return render(request, 'helpApp/checksubject.html', context)

def settingtable(request):
    if 'search-subject' in request.GET:
        q = request.GET.get('search-subject')
        #subject = Subject.objects.filter(subject_ID__icontains=q)
        multi_q = Q(Q(subject_ID__icontains=q) | Q(name__icontains=q))
        subject = Subject.objects.filter(multi_q)
    else:
        subject = Subject.objects.all()
    return render(request, 'helpApp/settingtable.html', {'subject':subject})

def verify(request, subject_ID):
    subject = Subject.objects.get(id=subject_ID)
    return render(request, 'helpApp/checking.html',{'subject':subject})
