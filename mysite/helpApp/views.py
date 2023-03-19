from django.shortcuts import render
from django.http import HttpResponse
from .models import Section, Subject
from userApp.models import User_subject
from django.db.models import Q
from django.http import JsonResponse
from .user_subject_manage import subject_manage

def studyTimetable(request):
    course = User_subject.objects.all()
    period = ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
    return render(request, 'helpApp/studytimetable.html', {'course':course, 'period':period})

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

def add_subject_request(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        m = subject_manage()
        m.add_subject("testuser123456", subject_id, "S.1")

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'})
