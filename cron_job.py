#!/usr/bin/env python3
from crontab import CronTab
    
#init cron
cron = CronTab(user='pi')
cron.remove_all()

#add new cron job
job  = cron.new(command='/home/pi/Sensors_Database/sense_data.py')

#job settings
job.minute.every(2)
cron.write()
