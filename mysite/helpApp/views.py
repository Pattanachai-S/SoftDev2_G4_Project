from django.shortcuts import render
from django.http import HttpResponse
from .models import Section, Subject
from userApp.models import User_subject
from django.db.models import Q,F
from django.http import JsonResponse
from django.contrib.auth.models import User
from .user_subject_manage import subject_manage
from .check_overlap import Overlap
from django.shortcuts import redirect

def studyTimetable(request):
    if request.user.is_authenticated:
        courses = User_subject.objects.filter(user_id=request.user)

        time_used = {'M': [], 'T': [], 'W': [], 'H': [], 'F': [], 'S': []}
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
        course_mid = User_subject.objects.filter(user_id=request.user).order_by(F('section__subject_ID__mid_term_date').asc(nulls_last=True))
        course_fin = User_subject.objects.filter(user_id=request.user).order_by(F('section__subject_ID__final_term_date').asc(nulls_last=True))
        return render(request, 'helpApp/examtimetable.html', {'course_m': course_mid, 'course_f': course_fin})
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
    courses = User_subject.objects.filter(user_id=request.user)
    q = request.GET.get('search-subject', '')
    if q:
        multi_q = Q(Q(subject_ID__icontains=q) | Q(name__icontains=q))
        subject = Subject.objects.filter(multi_q).exclude(section__in=courses.values_list('section', flat=True))
    else:
        subject = Subject.objects.exclude(section__in=courses.values_list('section', flat=True))
    context = {
        'subject': subject,
        'course': courses,
        'qs': q,
    }
    return render(request, 'helpApp/settingtable.html', context)
def verify(request, subject_ID):
    subject = Subject.objects.get(id=subject_ID)
    return render(request, 'helpApp/checking.html',{'subject':subject})

def add_subject_request(request):
    if request.user.is_authenticated:
        user_name = request.user.username  
        user_pk = request.user.pk  # user_pk is an integer
        subject = Subject.objects.all()
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            sec_num = request.POST.get('section')

            m = subject_manage()
            if "add_btn" in request.POST:
                if m.can_submit(user_name, subject_id, sec_num):
                    print("Add", user_name, subject_id, sec_num)
                    m.add_subject(user_name, subject_id, sec_num)
                return redirect(settingtable)
                    
            if "del_btn" in request.POST:
                print("Delete", user_name, subject_id, sec_num)
                m.remove_subject(user_name, subject_id, sec_num)
                return redirect(studyTimetable)

            # return JsonResponse({'success': True}, status=400)
            # return render(request, 'helpApp/settingtable.html', {'subject':subject})
            

        else:
            subject = Subject.objects.all()
            return redirect(settingtable)
        
def testfinal1(request):
    courses = User_subject.objects.all()
    q = request.GET.get('search-subject', '')
    if q:
        multi_q = Q(Q(subject_ID__icontains=q) | Q(name__icontains=q))
        subject = Subject.objects.filter(multi_q).exclude(section__in=courses.values_list('section', flat=True))
    else:
        subject = Subject.objects.exclude(section__in=courses.values_list('section', flat=True))
    context = {
        'subject': subject,
        'course': courses,
        'qs': q,
    }
    return render(request, 'helpApp/test1.html', context)

def testfinal2(request):
    subjects = Subject.objects.all()

    num_users = {}
    for subject in subjects:
        sections = Section.objects.filter(subject_ID=subject)
        user_subjects = User_subject.objects.filter(section__in=sections).values('user_id').distinct()
        num_users[subject.subject_ID] = user_subjects.count()

    return render(request, 'helpApp/test2.html', {'subject': subjects, 'num_users': num_users})
