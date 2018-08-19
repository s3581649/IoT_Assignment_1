"""
REFERENCE: This script was taken from the RMIT IoT Tute/Lab Code Archive and slightly modified
"""
#import sqlite3 and system modules
import sqlite3 as lite
import sys

#connects to database and creates a new table with datetime, temperature and humidity columns
connection = lite.connect('sensehat.db')
with connection:
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")