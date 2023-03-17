from datetime import datetime, time

class Overlap():

    def is_day_overlap(self, first_sub, second_sub):
        """Return ture if overlap"""
        if first_sub == second_sub:
            return True
        
    def is_time_overlap(self, first_sub, second_sub):
        """Return ture if overlap
        Input format 13:00-16:00"""

        # Find start-end of frist
        first_sub = first_sub.split("-")
        start1 = first_sub[0]
        end1 = first_sub[1]

        # Find start-end of second_sub
        second_sub = second_sub.split("-")
        start2 = second_sub[0]
        end2 = second_sub[1]

        time_format = '%H:%M'  # format of time
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

if __name__ == "__main__":
    c = Overlap()
    # all test is Ture or Overlap
    print(c.is_time_overlap("9:00-12:00","9:00-12:00"))
    print(c.is_time_overlap("13:00-15:00","12:00-14:00"))
