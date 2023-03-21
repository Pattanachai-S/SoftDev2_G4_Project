from bs4 import BeautifulSoup
from django.db import models
import os 
from datetime import datetime
import sqlite3
from update_time_db import subject as update_subject
from update_time_db import section as update_section
class Scraping():
    
    def __init__(self) -> None:
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def scrap_subject(self):
        """For Subject"""
        os.chdir(self.dir_path)
        file = "dataQuerySelector.html"

        # Open the HTML file
        with open(file, 'r', encoding="cp874") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        # find all subject
        table = soup.find('table', attrs={'align': 'center', 'border': '1', 'cellpadding': '2', 'cellspacing': '0', 'width': '100%', 'bordercolor': '#CCCCCC'})

        self.subject_list = []
        # Loop through the tr and td elements of the table
        for row in table.find_all('tr'):
            subject = []
            for cell in row.find_all('td'):
                # Print the contents of each td element
                text = cell.get_text()
                text = text.replace('\n\t\t', '')  # Remove void line 
                text = text.replace('  ', ' ')  #  change double space to one space 
                text = text.replace('\xa0', ' ')
                subject.append(text)
            self.subject_list.append(subject)
        self.subject_list.pop(0)


    def show_data(self):
        for row in self.subject_list:
            print("---------------")
            for cell in row:
                print(cell)

    def save_to_database(self):
        os.chdir(self.dir_path)
        os.chdir("../")
        conn = sqlite3.connect('db.sqlite3')
        # Create a cursor object to interact with the database
        c = conn.cursor()
        # Insert data into the table
        for subject in self.subject_list:
            print(subject)
            subject_id = subject[0][0:9]
            subject_name = subject[0][10:]
            mid_term = subject[1]
            final = subject[2]
            c.execute("INSERT INTO helpApp_subject (subject_ID, name, mid_term, final) VALUES (?, ?, ?, ?)", (subject_id,subject_name,mid_term,final))
        conn.commit()  # Save changes to the database
        conn.close()  # Close the connection
        
    # not use
    def convert_to_date_format(self, date):
        print(date)
        if date != " ":
            date = date.split(" ")
            print(date)
            date_str = date[1] + " " + date[2]
            date_format = "%d/%m/%Y %H:%M-%H:%M"
            date_time = datetime.strptime(date_str, date_format)
            return date_time
        else:
            return " "
    
    def clear_table(self):
        import sqlite3

        # Create a connection to the database
        os.chdir(self.dir_path)
        os.chdir("../")
        conn = sqlite3.connect('db.sqlite3')      
        c = conn.cursor()  # Create a cursor object to interact with the database
        
        # Execute a DELETE statement to clear all data from the table
        c.execute("DELETE FROM helpApp_subject")
        c.execute("DELETE FROM helpApp_section")

        conn.commit() # Save changes to the database     
        conn.close() # Close the connection

    def scrap_section(self):       
        """For Section"""

        os.chdir(self.dir_path)
        file_Sec = "dataQuerySelectorSec.html"
        with open(file_Sec, 'r', encoding="cp874") as file_Sec:
            html_content = file_Sec.read()
        soup = BeautifulSoup(html_content, 'html.parser')

        # subject_name_list = soup.find_all('tr', attrs={'bgcolor': '#EA98FF'})
        # section_list =  soup.find_all('tr', attrs={'bgcolor': '#F1F1FD'})

        # # find all subject id
        # subject_id_list = []
        # for text in subject_name_list:
        #     subject = text.find("b")
        #     subject_id_list.append(subject.get_text()[0:9])

        # sec_list = []
        # for text in section_list:
        #     sec_number = text.find('td',attrs={'valign':'top'}).get_text()
        #     sec_info = text.find('tbody')
        #     sec_day = sec_info.find('td',attrs={'width':'7%'}).get_text()
        #     sec_time = sec_info.find('td',attrs={'width':'25%'}).get_text()
        #     sec_teacher = sec_info.find('td',attrs={'width':'46%'}).get_text().replace("\xa0","")
        #     sec_list.append([sec_number,sec_day,sec_time,sec_teacher])


        # find subject id and all sec
        subject_and_sec = []
        sub = soup.find_all('tr')

        for text in sub:
            t = text.find("b")
            if t != None:
                # print(t.get_text())
                s = t.get_text().split(" ")
                subject_id = s[0]
                

            sec_number = text.find('td',attrs={'valign':'top'})
            if sec_number != None:
                # print(sec_number.get_text())
                sec_number = sec_number.get_text()
               
            # sec_info = text.find('tbody')
            # soup2 = BeautifulSoup(text, 'html.parser')
            in_text = text.find_all('td',attrs={'width':'61%'})
            for txt2 in in_text:
                in_text2 = txt2.find_all('table',attrs={'width':'100%'})
                for t in in_text2:
                    sec_info_list = t.find_all('tbody')
                    for t2 in sec_info_list:
                        sec_info_list2 =t2.find_all('tr')
                        for sec_info in sec_info_list2:
                            if sec_info != None:
                                sec_day = sec_info.find('td',attrs={'width':'7%'})
                                if sec_day != None:
                                    # print(sec_day.get_text())
                                    sec_day = sec_day.get_text()

                                sec_time = sec_info.find('td',attrs={'width':'25%'})
                                if sec_time != None:
                                    # print(sec_time.get_text())
                                    sec_time = sec_time.get_text()

                                sec_teacher = sec_info.find('td',attrs={'width':'46%'})
                                if sec_teacher != None:
                                    # print(sec_teacher.get_text())
                                    sec_teacher = sec_teacher.get_text().replace("\xa0","")

                                sec_info = [sec_number,sec_day,sec_time,sec_teacher]
                                subject_and_sec.append([subject_id,sec_info])
        # subject_and_sec.pop(0)  # remove text คณะ....
        self.subject_and_sec = subject_and_sec

    def show_data_sec(self):
        for sns in self.subject_and_sec:
            print(sns)
            pass


    #     print(subject_id_list)
    #     print(sec_list)

    #     sec_list_index = 0
    #     subject_and_sec = []
    #     for subject_id in subject_id_list:
    #         sec = []     
    #         while(self.next_sec(sec_list[sec_list_index])):
    #             sec.append(sec_list[sec_list_index])
    #             sec_list_index += 1
    #         subject_and_sec.append([subject_id,sec])
                
    # def next_sec(self):


    def save_sec_to_database(self):
        # connect to the database
        os.chdir(self.dir_path)
        os.chdir("../")
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor() # create a cursor object

        # # execute a SELECT statement to search for records
        # cur.execute("SELECT subject_id FROM helpApp_subject")    
        # results = cur.fetchall()  # fetch the results

        for sns in self.subject_and_sec:
            subject_id = sns[0]
            sec_number = sns[1][0]
            sec_day = sns[1][1]
            sec_time = sns[1][2]
            sec_teacher = sns[1][3]
            # Get the user ID
            subject_id = conn.execute("SELECT id FROM helpApp_subject WHERE subject_ID=?", (subject_id,)).fetchone()[0]
            cur.execute("INSERT INTO helpApp_section (subject_ID_id, sec_num, day, time, teacher) VALUES (?, ?, ?, ?, ?)", (subject_id,sec_number,sec_day,sec_time,sec_teacher))

        conn.commit()  # Save changes to the database
        conn.close()  # Close the connection



def scraping():
    scraping = Scraping()

    """for clear old data"""
    scraping.clear_table()
    
    """for scrap subject"""
    scraping.scrap_subject()
    scraping.show_data()
    scraping.save_to_database() 
    sub = update_subject()
    sub.update()

    """for scrarp section"""
    scraping.scrap_section()
    scraping.show_data_sec() 
    scraping.save_sec_to_database()
    sec = update_section()
    sec.update()

    
   
if __name__ == "__main__":
    scraping()
    


