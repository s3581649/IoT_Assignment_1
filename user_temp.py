#!/usr/bin/env python3

#Request user input 
temp_threshold = input("Please input a temperature threshold: ")
#Open txt file and store user input for later use
with open('/home/pi/Assignment_1/user_temperature.txt', 'w') as file:
    file.write(str(temp_threshold))
    file.close()