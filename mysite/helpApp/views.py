from django.shortcuts import render,get_object_or_404
from .models import Section, Subject
from django.db.models import Q

def studyTimetable(request):
    return render(request, 'helpApp/studytimetable.html')

def examTimetable(request):
    return render(request, 'helpApp/examtimetable.html')

def checkSubject(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        #subject = Subject.objects.filter(subject_ID__icontains=q)
        multi_q = Q(Q(subject_ID__icontains=q) | Q(name__icontains=q))
        subject = Subject.objects.filter(multi_q)
    else:
        subject = Subject.objects.all()
    context = {'subject':subject}
    return render(request, 'helpApp/checksubject.html', context)

def settingtable(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        #subject = Subject.objects.filter(subject_ID__icontains=q)
        multi_q = Q(Q(subject_ID__icontains=q) | Q(name__icontains=q))
        subject = Subject.objects.filter(multi_q)
    else:
        subject = Subject.objects.all()
    context = {'subject':subject}
    return render(request, 'helpApp/settingtable.html', context)

def subjectsetting(request, subject_ID):
    subject = get_object_or_404(Subject, pk=subject_ID)
    return render(request, 'helpApp/selectsubject.html', {'subject':subject})

