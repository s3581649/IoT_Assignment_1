import senseData_module as sd
import pushBullet as pb
import SenseHat
import os
import time
import sqlite3
dbname='sensehat.db'

def setTempAndHumidity():
    sense = SenseHat()
    temp = sd.getSensehatTemp(sense)
    humidity = sd.getSensehatHumidity(sense)
    logData(temp,humidity)
    sense.clear()
    return(temp)

def logData(temp,humidity):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?))", (temp,),(humidity,))
    conn.commit()
    conn.close()

def displayLog():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SenseHat_data"):
        print (row)
    conn.close()

#main function
def main():
    setTempAndHumidity()
    temp = setTempAndHumidity()
    displayLog()

    if temp > 20:
        ip_address = os.popen('hostname -I').read()
        pb.send_notification_via_pushbullet(ip_address, "It is below 20C, Please remember to bring a sweater")

#Execute
main()
