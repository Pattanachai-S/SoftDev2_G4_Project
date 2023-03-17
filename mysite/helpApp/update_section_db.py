from bs4 import BeautifulSoup
from django.db import models
import os 
from datetime import datetime
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))

class section():

    def __init__(self) -> None:
        pass

    def update(self):
        os.chdir(dir_path)
        os.chdir("../")
        conn = sqlite3.connect('db.sqlite3')

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a SELECT query to retrieve all rows from the table
        cursor.execute('SELECT * FROM helpApp_section')

        # Fetch all the rows returned by the query
        rows = cursor.fetchall()

        # Iterate over the rows and add data to the last column
        for row in rows:
            # assuming the last column is column 8
            new_value = "new data"
            row_data = list(row)
            row_data[8] = new_value
            updated_row = tuple(row_data)
            # update the row with the new data
            cursor.execute('UPDATE my_table SET column4 = ? WHERE id = ?', (updated_row[3], updated_row[0]))

        # Commit the changes to the database
        conn.commit()

        # Close the database connection
        conn.close()