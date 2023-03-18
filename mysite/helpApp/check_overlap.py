
import os
import django
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
os.chdir("../")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from datetime import datetime, time
import os 
import sqlite3
from django.db import models
from models import Subject,Section



class Overlap():

    def is_day_overlap(self, first_sub, second_sub):
        """Return True if overlap"""
        if first_sub == second_sub:
            return True
        else:
            return False
        
    def is_time_overlap(self, first_sub, second_sub):
        """Return True if overlap
        Input format 13:00-16:00"""

        # Find start-end of frist
        first_sub = first_sub.split("-")
        start1 = first_sub[0]
        end1 = first_sub[1]

        # Find start-end of second_sub
        second_sub = second_sub.split("-")
        start2 = second_sub[0]
        end2 = second_sub[1]

        # Convert to time
        time_format = '%H:%M'  # format of string
        start1 = datetime.strptime(start1, time_format).time()
        end1 = datetime.strptime(end1, time_format).time()
        start2 = datetime.strptime(start2, time_format).time()
        end2 = datetime.strptime(end2, time_format).time()

        if end1 <= start2 or start1 >= end2:
            # if 1st_subject end before 2nd start
            # or 1st_subject start after 2nd end
            return False  # It can not overlap
        else:
            return True


    def is_overlap(self, first_sub, second_sub):
        """Return True if overlap
            Input: ['M',"09:00-12:00"]"""
        
        # check study day
        if ( not(self.is_day_overlap(first_sub[0], second_sub[0]))):
            return False  # If do not study in same day return False 
        
        # check study time
        if ( not(self.is_time_overlap(first_sub[0], second_sub[0]))):
            return False # If do not study in same time return False 
        else:
            return True
        
    def is_subject_overlap(self, first_sub, second_sub):
        """Return True if overlap
            Input: [['subject_code','sec']]"""
        
        code1 = first_sub[0]
        code2 = second_sub[0]

        # Find exam time in database
        mid_term_col = "mid_term"
        final_col = "final"
        # 1st subject
        sub1 = Subject.objects.filter(subject_ID=code1).values(mid_term_col, final_col)
        print(sub1)

            


        
if __name__ == "__main__":
    c = Overlap()
    # all test is Ture or Overlap
    print(c.is_time_overlap("9:00-12:00","9:00-12:00"))
    print(c.is_time_overlap("13:00-15:00","12:00-14:00"))

    print(c.is_subject_overlap(['010113138','S.1'],['010123124','S.1']))
