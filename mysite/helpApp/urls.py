from django.urls import path
from . import views

urlpatterns = [
    path('studytimetable', views.studyTimetable, name='study'),
    path('examtimetable', views.examTimetable, name='exam'),
    path('checksubject', views.checkSubject, name='check'),
    path('settingtimetable', views.settingtable, name='table'),
    path('check/<int:subject_ID>', views.verify, name='verify'),
]