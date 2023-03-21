from django.urls import path
from . import views
from .user_subject_manage import subject_manage

urlpatterns = [
    path('studytimetable', views.studyTimetable, name='study'),
    path('examtimetable', views.examTimetable, name='exam'),
    path('checksubject', views.checkSubject, name='check'),
    path('settingtimetable', views.settingtable, name='table'),
    path('verify/<int:subject_ID>', views.verify, name='verify'),
    path('add_subject', views.add_subject_request, name='add_subject'),
    path('add_subject2', views.add_subject_request2, name='add_subject2'),
]