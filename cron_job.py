#!/usr/bin/env python3
"""
REFERENCE: This script was partially taken from the RMIT IoT Tute/Lab Code Archive
"""
#import cron tab module
from crontab import CronTab
    
#initialises the cron job
cron = CronTab(user='pi')
cron.remove_all()

#add new cron job
job  = cron.new(command='/home/pi/Assignment_1/senseData_App.py')

#schedule job to every 5min
job.minute.every(5)
cron.write()
