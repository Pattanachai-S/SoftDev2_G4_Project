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



sec = section()
sec.update()