import senseData_module as sd
import SenseHat
import time
import sqlite3
dbname='sensehat.db'

def setTemp():
    sense = SenseHat()
    temp = sd.getSensehatTemp(sense)
    logData(temp)

def logData(temp):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?))", (temp,))
    conn.commit()
    conn.close()
