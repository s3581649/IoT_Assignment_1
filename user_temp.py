#!/usr/bin/env python3

#Ask the user for temperature input
temp_threshold = input("Please input a temperature threshold: ")
#Save the temperature to a file for later access
with open('/home/pi/Assignment_1/user_temperature.txt', 'w') as file:
    file.write(str(temp_threshold))
    file.close()