from django.shortcuts import render
from django.http import HttpResponse
from .models import Section, Subject
from userApp.models import User_subject
from django.db.models import Q

def studyTimetable(request):
    if request.user.is_authenticated:
        courses = User_subject.objects.filter(user_id=request.user)

        time_used = {'M': [], 'T': [], 'W': [], 'H': [], 'F': []}
        times = ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
        for course in courses:
            day = course.section.day
            start_t = course.section.start_time
            end_t = course.section.end_time
            keep = False
            for time in times:
                if start_t == time:
                    keep = True
                if end_t == time:
                    keep = False
                if (keep): 
                    time_used[day].append(time)
                
        return render(request, 'helpApp/studytimetable.html', {'course':courses, 'time':times, 'time_usedd':time_used})
    else:
        return render(request, 'helpApp/studytimetable.html')

def examTimetable(request):
    if request.user.is_authenticated:
        course = User_subject.objects.filter(user_id=request.user)
        return render(request, 'helpApp/examtimetable.html', {'course':course})
    else:
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

def verify(request, subject_ID):
    subject = Subject.objects.get(id=subject_ID)
    return render(request, 'helpApp/checking.html',{'subject':subject})
