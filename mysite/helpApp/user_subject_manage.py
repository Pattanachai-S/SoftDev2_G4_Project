import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from helpApp.models import Subject,Section
from userApp.models import User_subject
from django.http import JsonResponse
class subject_manage():

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


if __name__ == "__main__":
    m = subject_manage()
    m.add_subject("testuser123456", "010113138", "S.1")