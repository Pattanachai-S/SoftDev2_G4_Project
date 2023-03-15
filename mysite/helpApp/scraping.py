from bs4 import BeautifulSoup
from django.db import models
import os 
from datetime import datetime
import sqlite3

class Scraping():
    
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
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
                subject.append(text.replace('\n\t\t', '').replace('  ', ' '))
            self.subject_list.append(subject)

    def show_data(self):
        for row in self.subject_list:
            print("---------------")
            for cell in row:
                print(cell)

    def save_to_database(self):
        os.chdir(self.dir_path)
        os.chdir("../")
        print(os.getcwd())
        conn = sqlite3.connect('db.sqlite3')
        # Create a cursor object to interact with the database
        c = conn.cursor()
        # Insert data into the table
        for subject in self.subject_list:
            print(subject)
            if subject != ['วิชาที่เปิดใน 2/2565', 'กลางภาค', 'ปลายภาค']:
                subject_id = subject[0][0:9]
                subject_name = subject[0][10:]
                mid_term = subject[1]
                final = subject[2]
                c.execute("INSERT INTO helpApp_subject (subject_ID, name, mid_term, final) VALUES (?, ?, ?, ?)", (subject_id,subject_name,mid_term,final))
        conn.commit()  # Save changes to the database
        conn.close()  # Close the connection
        
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
    

    
if __name__ == "__main__":
    scraping = Scraping()
    scraping.show_data()
    scraping.save_to_database()
    


