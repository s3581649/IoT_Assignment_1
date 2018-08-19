# IoT_Assignment_1
RASPBERYY PI TEMPERATURE AND HUMIDITY APPLICATION

OVERVIEW:
This python application is designed to read and store temperature and humidity data
from the sensehat module, then visualise it using Flask and Dash web microframework.

Project Contents
_________________

bluetooth_app.py: When run this script will search for nearby devices based on inputted credintials. 
Once located it then greets the owner with the phone and triggers the sensehat to display the current
temperature.

cron_job.py: When run this script will run the scheduled file(the main application) every 5 minutes.

database.py: When run this script will create a sensehat database with a table containing 3 columns 
consisting of datetime, temperature and humidity.

pushBullet.py: This code's purpose is to serve as a module for the main application. When utilised it
allows the main application a pushbullet notification when the if condition for temperature is met.

senseData_app: This is the main application. It utilises both pushbullet and custom sensedata modules to 
extract temperature from the sensehat and then log it into the database.

senseData_module: This is a custom sensehat modules that once run will capture and calibrate the temperatures 
from the sensehat by subtracting the cpu's temperature from the actual received data.

user_temp.py: This script allows for user input that can then be used as a temperature threshold for the
pushbullet if condition.

web_App.py: This script is used to visualise the data stored by the database into a graph.