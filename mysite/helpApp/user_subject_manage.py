from .models import Section, Subject
from userApp.models import User_subject
from django.contrib.auth.models import User
from .check_overlap import Overlap


class subject_manage():
    pass

    def add_subject(self, user_name, subject, section):
        """ Input: 'username', 'subject_code', 'section_subject' """
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
        """ Input: 'username', 'subject_code', 'section_subject' """
        # Remove section_subject in database for user
        # Get user_id and sec_id
        user = User.objects.get(username = user_name)
        sub = Subject.objects.get(subject_ID = subject)

        if section != None:
            sec_list = Section.objects.filter(subject_ID = sub, sec_num = section)
        else:
            sec_list = Section.objects.filter(subject_ID = sub)
           
        for sec in sec_list:   
            user_subject = User_subject.objects.filter(user_id = user, section = sec)  # Get object
            user_subject.delete()  # remove from database







    def can_submit(self, user_name, subject_id, sec_num):
        """Input: 'username', 'subject_code', 'section_subject'"""
        # Check all Section what user choose in database can submit

        o = Overlap()
        user = User.objects.get(username = user_name)
        list_subject = User_subject.objects.filter(user_id = user)
        for s in list_subject:
            section1 = Section.objects.get(id = s.section_id)
            if o.is_subject_overlap([section1.subject_ID.subject_ID, section1.sec_num], [subject_id, sec_num]):
                 return False
        
        # If have not any overlap
        return True  