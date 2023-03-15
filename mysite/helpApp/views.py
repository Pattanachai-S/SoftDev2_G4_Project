from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Section, Subject
from django.db.models import Q

def studyTimetable(request):
    return render(request, 'helpApp/studytimetable.html')

def examTimetable(request):
    return render(request, 'helpApp/examtimetable.html')

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

def checking(request, subject_ID):
    subject = Subject.objects.all()
    return render(request, 'helpApp/checking.html',{'subject':subject})
