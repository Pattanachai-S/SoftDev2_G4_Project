from django.urls import path
from . import views

urlpatterns = [
    path('studytimetable', views.studyTimetable, name='study'),
    path('examtimetable', views.examTimetable, name='exam'),
    path('checksubject', views.checkSubject, name='check'),
    path('settingtimetable', views.settingtable, name='table'),
    path('add_subject', views.add_subject_request, name='add_subject'),
    path('sumary_subject', views.sumarySubject, name='sumary_subject'),
    path('verify/<int:subject_ID>', views.verify, name='verify'),
]