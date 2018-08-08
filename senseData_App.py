import senseData_module as sd
import pushBullet as pb
from sense_hat import SenseHat
import os
import time
import sqlite3
dbname='sensehat.db'

def setTempAndHumidity():
    sense = SenseHat()
    temp = sd.getTemp(sense)
    humidity = sd.getHumidity(sense)
    logData(temp,humidity)
    sense.clear()
    
    if temp < 20:
        ip_address = os.popen('hostname -I').read()
        pb.send_notification_via_pushbullet(ip_address, "It is below 20C, Please remember to bring a sweater")

def logData(temp,humidity):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?))", (temp,humidity))
    conn.commit()
    conn.close()

    displayLog(temp)

def displayLog(temp):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SenseHat_data"):
        print (row)
    conn.close()

    sense = SenseHat()
    sense.show_message('Time is {}'.format(temp), scroll_speed=0.05)

#main function
def main():
    setTempAndHumidity()

#Execute
main()
