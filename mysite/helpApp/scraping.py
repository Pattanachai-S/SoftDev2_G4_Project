from bs4 import BeautifulSoup
from django.db import models
import os 
from datetime import datetime
from helpApp.models import Subject

class Scraping():
    
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(dir_path)
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
                subject.append(text.replace('\n\t\t', ''))
            self.subject_list.append(subject)

    def show_data(self):
        for row in self.subject_list:
            print("---------------")
            for cell in row:
                print(cell)

    def save_to_database(self):
        for subject in self.subject_list:
            
            subject_id = subject[0][0:9]
            subject_name = subject[0][10:]
            mid_term = self.convert_to_date_format(subject[1])
            final = self.convert_to_date_format(subject[2])

            s = Subject(subject_ID=subject_id,
                    name=subject_name,
                    mid_term=mid_term,
                    final=final)
            s.save()

    def convert_to_date_format(self, date):
        date = date.split(" ")
        date_str = date[1] + " " + date[2]
        date_format = "%d/%m/%Y %H:%M-%H:%M"
        date_time = datetime.strptime(date_str, date_format)
        return date_time
    

    
if __name__ == "__main__":
    scraping = Scraping()
    scraping.save_to_database()


