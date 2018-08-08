import os
from sense_hat import SenseHat

def getSensehatHumidity(sense_obj):
    humidity = sense.get_humidity()
    return(humidity)
    
def getSensehatTemp(sense_obj):
    #Getting temperature from sensehat temperature sensor
    temp = sense_obj.getSensehatTemp()
    #Getting temperature from the CPU of the Raspberry Pi
    res = os.popen("vcgencmd measure_temp").readline()
    cpu_temp = float(res.replace("temp=","").replace("'C/n",""))
    #Running Calabiration Method
    calabirateTemp(temp,cpu_temp)

#Calabirating the temperature using the below formula with a factor of 5.466
#Factor was taken from the following site: 
#https://github.com/initialstate/wunderground-sensehat/blob/master/sensehat_darksky_calibrated.py (line 124)
def calabirateTemp(temp,cpu_temp):
    calab_temp = temp - ((cpu_temp-temp)/5.466)
    return(round(calab_temp,1)