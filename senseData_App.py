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
    pushbullet_notification(temp)
    sense.clear()

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

def pushbullet_notification(temp):
    file = open('/home/pi/Assignment_1/user_temperature.txt', 'r')
    temp_threshold = file.read(2)
    
    if temp < int(temp_threshold):
        pb.send_notification_via_pushbullet("Wheather Update!", "It is below " + temp_threshold + "C, Please remember to bring a sweater")

#main function
def main():
    setTempAndHumidity()

#Execute
main()
