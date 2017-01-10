#!/usr/bin/python
#coding=utf8
from datetime import datetime
import os

def LLV(datas):
    return min(datas)

def HHV(datas):
    return max(datas)

def CROSS(values1=[1,2],values2=[3,4]):
    v10 = values1[0]
    v11 = values1[1]
    v20 = values2[0]
    v21 = values2[1]
    if(v10<v20 & v11>v21):
        print('上穿')
        return True
    else:
        print('没有上穿')
        return False
 
def MA(datas):
    count = 0
    for data in datas:
        count = count + data
    return count/len(datas)

def SMA(datas,N=1):
    length = len(datas)
    return (datas[0]*(N+1) + total(datas[1:length]))/(length+N)
        
def total(datas):
    return len(datas)

def dataFrameToArray(datasArray):
    return [round(data[0], 3) for data in datasArray]

    
# def scheWithTrigger(name ,year=None, month=None, day=None, week=None, day_of_week=None, hour=None,
#                  minute=None, second=None, start_date=None, end_date=None, timezone=None):
#     scheduler = BlockingScheduler()
#     trigger = CronTrigger(year=year, month=month, day=day, week=week, day_of_week=day_of_week, hour=hour,
#                  minute=minute, second=second, start_date=start_date, end_date=end_date, timezone=timezone)
#     scheduler.add_job(name,trigger=trigger)
#     print('Listen start! %s' % datetime.now())
#
#     try:
#         scheduler.start()
#     except (KeyboardInterrupt,SystemExit):
#         pass
#
    