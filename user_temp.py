#!/usr/bin/env python3

temp_threshold = input("Please input a temperature threshold: ")
with open('/home/pi/Assignment_1/user_temperature.txt', 'w') as file:
    file.write(str(temp_threshold))
    file.close()