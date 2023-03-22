from datetime import datetime, time
from helpApp.models import Subject,Section



class Overlap():

    def is_same_day(self, first_sub, second_sub):
        """Return True if the same"""
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
        if ( not(self.is_same_day(first_sub[0], second_sub[0]))):
            return False  # If do not study in same day return False 
        
        # check study time
        if ( not(self.is_time_overlap(first_sub[1], second_sub[1]))):
            return False # If do not study in same time return False 
        else:
            return True
        
    def is_both_have_exam(self, first_sub, second_sub):
        if len(first_sub) >= 3 and len(second_sub) >= 3:  # have date and time
            return True
        else:
            return False

    def is_subject_overlap(self, first_sub, second_sub):
        """Return True if overlap
            Input: [['subject_code','sec']]"""
        
        code1 = first_sub[0]
        code2 = second_sub[0]
        sec_num1 = first_sub[1]
        sec_num2 = second_sub[1]

        # Find exam time in database
        mid_term_col = "mid_term"
        final_col = "final"
        # 1st subject
        sub1 = Subject.objects.filter(subject_ID=code1)
        sub1 = sub1[0] # Get 1st query
        mid1 = sub1.mid_term.split(" ")  # พฤ. 30/3/2566 13:00-16:00
        final1 = sub1.final.split(" ")
        # 2nd subject
        sub2 = Subject.objects.filter(subject_ID=code2)
        sub2 = sub2[0] # Get 1st query
        mid2 = sub2.mid_term.split(" ")  #พฤ. 30/3/2566 13:00-16:00
        final2 = sub2.final.split(" ")

        # Check exam date
        if (self.is_both_have_exam(mid1,mid2) and self.is_overlap(mid1[1:],mid2[1:])): 
                # midterm
                return True
        if (self.is_both_have_exam(final1,final2) and self.is_overlap(final1[1:],final2[1:])):
                # final  
                return True

        # Find study day-time in database
        sec1 = Section.objects.filter(subject_ID = sub1, sec_num = sec_num1)
        sec2 = Section.objects.filter(subject_ID = sub2, sec_num = sec_num2)
        # loop for subject have 2 day study case
        for sec_sub1 in sec1:
            for sec_sub2 in sec2:
                if (self.is_overlap([sec_sub1.day, sec_sub1.time], [sec_sub2.day, sec_sub2.time])):
                    return True  # If have any overlap will return True
                
        # return False after check exam date-time and study day-time is do not overlap
        return False

