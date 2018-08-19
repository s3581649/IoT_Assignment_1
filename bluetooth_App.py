#!/usr/bin/env python3
"""
REFERENCE: This script was partially taken from the RMIT IoT Tute/Lab Code Archive
"""
#importing modules
import bluetooth
import os
import time
from sense_hat import SenseHat
import senseData_module as sd

# Search for device based on device's name
def search_devices(user_name, device_name):
    while True:
        device_address = None
        dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
        print("\nCurrently: {}, searching for {}".format(dt, device_name))
        time.sleep(3) #Sleep three seconds 
        nearby_devices = bluetooth.discover_devices()

        for mac_address in nearby_devices:
            if device_name == bluetooth.lookup_name(mac_address, timeout=5):
                device_address = mac_address
                break
        if device_address is not None:
            sense = SenseHat()
            sense.show_message("Device ({}) was found! Hello ({}) your MAC address is: {}".format(device_name, user_name, device_address), scroll_speed=0.04)
            temp = sd.getTemp(sense)
            sense.show_message("Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed=0.05)
        else:
            print("Was not able to detect {}, please try again!".format(device_name))

# Main function, requests user input for name and phone name
def main():
    user_name = input("Enter your name: ")
    device_name = input("Enter the name of your phone: ")
    search_devices(user_name, device_name)

#Execute program
main()
