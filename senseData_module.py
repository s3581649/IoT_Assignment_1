import os
from sense_hat import SenseHat

def getHumidity(sense_obj):
    humidity = sense_obj.get_humidity()
    return(humidity)
    
def getTemp(sense_obj):
    #Getting temperature from sensehat temperature sensor
    temp = sense_obj.get_temperature()

    #Getting temperature from the CPU of the Raspberry Pi
    res = os.popen('vcgencmd measure_temp').readline()
    cpu_temp = res.replace("temp=","").replace("'C\n","")
    
    #Running Calabiration Method
    return(calabirateTemp(temp,cpu_temp))

#Calabirating the temperature using the below formula with a factor of 5.466
#Factor was taken from the following site: 
#https://github.com/initialstate/wunderground-sensehat/blob/master/sensehat_darksky_calibrated.py (line 124)
def calabirateTemp(temp,cpu_temp):
    calab_temp = temp - ((float(cpu_temp)-temp)/1.5)
    return(round(calab_temp,1))