import sqlite3
import csv
import pandas as pd
from io import StringIO
import re


import sqlite3
import csv
import pandas as pd
from io import StringIO
import re

def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    header = [description[0] for description in cursor.description]
    csv_string = ','.join(header) + '\n'
    for row in rows:
        csv_string += ','.join(map(str, row)) + '\n'
    conn.close()
    return csv_string.strip()

def csv_to_sql(csv_content, database, table_name):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE volcanos (
            "Volcano Name" varchar(100),
            "Country" varchar(100),
            "Type" varchar(100),
            "Latitude (dd)" real,
            "Longitude (dd)" real,
            "Elevation (m)" real
            )
    ''')
    csv_data = csv_content.getvalue() 
    reader = csv.DictReader(csv_data.splitlines()) 
    to_db = [(i['Volcano Name'], i['Country'], i['Type'], i['Latitude (dd)'], i['Longitude (dd)'], i['Elevation (m)']) for i in reader]
    cursor.executemany("INSERT INTO volcanos (\"Volcano Name\", \"Country\", \"Type\", \"Latitude (dd)\", \"Longitude (dd)\", \"Elevation (m)\") VALUES (?, ?, ?, ?, ?, ?)", to_db)
    conn.commit()
    conn.close()