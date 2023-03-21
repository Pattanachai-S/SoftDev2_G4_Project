from django.shortcuts import render
from django.http import HttpResponse
from .models import Section, Subject
from userApp.models import User_subject
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.models import User

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

def add_subject_request(request):
    if request.user.is_authenticated:
        user_name = request.user.username  # user_id is an integer
        user_pk = request.user.pk  # user_pk is an integer
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            m = subject_manage()
            print(user_name, user_pk, "S.1")
            m.add_subject(user_name, subject_id, "S.1")

            # return JsonResponse({'success': True})
    
            # return JsonResponse({'error': 'Invalid request method'})
            subject = Subject.objects.all()
            return render(request, 'helpApp/settingtable.html', {'subject':subject})

        else:
            subject = Subject.objects.all()
            return render(request, 'helpApp/settingtable.html', {'subject':subject})
    

class subject_manage():
    pass

    def add_subject(self, user_name, subject, section):
        """ Input: 'username', 'sunject_code', 'section_subject' """
        # App section_subject to database for user

        # Get user_id and sec_id
        user = User.objects.get(username = user_name)
        sub = Subject.objects.get(subject_ID = subject)
        sec_list = Section.objects.filter(subject_ID = sub, sec_num = section)

        # Loop for subject have 2 day study case
        for sec in sec_list:   
            user_subject = User_subject(user_id = user, section = sec)  # Create object
            user_subject.save()  # Add to database

    def remove_subject(self, user_name, subject, section):
        """ Input: 'username', 'sunject_code', 'section_subject' """
        # Remove section_subject in database for user
        # Get user_id and sec_id
        user = User.objects.get(username = user_name)
        sub = Subject.objects.get(subject_ID = subject)
        sec_list = Section.objects.filter(subject_ID = sub, sec_num = section)

        # Loop for subject have 2 day study case
        for sec in sec_list:   
            user_subject = User_subject.objects.filter(user_id = user, section = sec)  # Get object
            user_subject.delete()  # remove from database


    def check_section_can_submit():
        # Check all Section what user choose in database can submit
        pass 