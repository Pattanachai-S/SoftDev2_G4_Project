import os 
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))

class section():

    def __init__(self) -> None:
        self.table_name = "helpApp_section"
        self.column_time_name = "time"
        self.column_start_time_name = "start_time"
        self.column_end_time_name = "end_time"
        
    def update(self):
        os.chdir(dir_path)
        os.chdir("../")
        print(os.getcwd())
        conn = sqlite3.connect('db.sqlite3')     
        self.cursor = conn.cursor() # Create a cursor object

        self.update_column()  # update data
            
        conn.commit()  # Commit the changes to the database
        conn.close() # Close the database connection

    def update_column(self):
        # Execute a SELECT query to retrieve all rows from the table
        self.cursor.execute('SELECT id, '+self.column_time_name+' FROM '+ self.table_name)

        # Fetch all the rows returned by the query
        rows = self.cursor.fetchall()
        for row in rows:

            row_data = list(row)
            print(row_data)

            # use time in row
            time_row = 1
            time = row_data[time_row].split("-")
            start_time = time[0]
            end_time = time[1]

            # update the row with the new data
            self.cursor.execute('UPDATE '+self.table_name+' SET '+self.column_start_time_name+' = ? WHERE id = ?', (start_time, row_data[0]))
            self.cursor.execute('UPDATE '+self.table_name+' SET '+self.column_end_time_name+' = ? WHERE id = ?', (end_time, row_data[0]))

class subject():

    def __init__(self) -> None:
        self.table_name = "helpApp_subject"
        self.mid_term = "mid_term"
        self.mid_term_date = "mid_term_date"
        self.mid_term_start_time = "mid_term_start_time"
        self.mid_term_end_time = "mid_term_end_time"
        self.final = "final"
        self.final_term_date = "final_term_date"
        self.final_term_start_time = "final_term_start_time"
        self.final_term_end_time = "final_term_end_time"
        
    def update(self):
        os.chdir(dir_path)
        os.chdir("../")
        print(os.getcwd())
        conn = sqlite3.connect('db.sqlite3')     
        self.cursor = conn.cursor() # Create a cursor object

        self.update_column(self.mid_term, self.mid_term_date, self.mid_term_start_time, self.mid_term_end_time)  # update data
        self.update_column(self.final, self.final_term_date, self.final_term_start_time, self.final_term_end_time)  # update data
            
        conn.commit()  # Commit the changes to the database
        conn.close() # Close the database connection

    def update_column(self, exam_date_col, date_col, start_time_col, end_time_col):
        # Execute a SELECT query to retrieve all rows from the table
        self.cursor.execute('SELECT id, '+exam_date_col+' FROM '+ self.table_name)
        
        # Fetch all the rows returned by the query
        rows = self.cursor.fetchall()
        for row in rows:

            row_data = list(row)
            # print(row_data)

            # use date in row
            exam_date_row = 1
            exam = row[exam_date_row]
            

            # have exam
            if len(exam) > 5:  # mean have a string in that cell

                exam = exam.split(" ")
                day = exam[0] 
                date = exam[1]
                time = exam[2]
                time = time.split("-")  # split start and end time
                start_time = time[0]
                end_time = time[1]


                # update the row with the new data
                self.cursor.execute('UPDATE '+self.table_name+' SET '+date_col+' = ? WHERE id = ?', (date, row_data[0]))
                self.cursor.execute('UPDATE '+self.table_name+' SET '+start_time_col+' = ? WHERE id = ?', (start_time, row_data[0]))
                self.cursor.execute('UPDATE '+self.table_name+' SET '+end_time_col+' = ? WHERE id = ?', (end_time, row_data[0]))
