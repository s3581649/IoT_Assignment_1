import senseData_module as sd
import SenseHat
import time
import sqlite3
dbname='sensehat.db'

def setTempAndHumidity():
    sense = SenseHat()
    temp = sd.getSensehatTemp(sense)
    humidity = sd.getSensehatHumidity(sense)
    logData(temp,humidity)
    sense.clear()

def logData(temp,humidity):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?))", (temp,),(humidity,))
    conn.commit()
    conn.close()

def displayLog():
    