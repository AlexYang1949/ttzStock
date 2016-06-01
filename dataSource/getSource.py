#!/usr/bin/python
#coding=utf8

# 定时任务
from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler
from astropy.units import second
from apscheduler.triggers.cron import CronTrigger

def tick():
    print('Tick! The time is :%s' % datetime.now())
    
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    trigger = CronTrigger(hour='9-12,13-19',minute='*',second='20,40')
    scheduler.add_job(tick,trigger=trigger)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    
    try:
        scheduler.start() 
    except (KeyboardInterrupt,SystemExit):
        pass