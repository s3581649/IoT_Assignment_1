#!/usr/bin/env python3
from crontab import CronTab
    
#init cron
cron = CronTab(user='pi')
cron.remove_all()

#add new cron job
job  = cron.new(command='/home/pi/Assignment_1/senseData_App.py')

#job settings
job.minute.every(5)
cron.write()
