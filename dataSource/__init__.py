#!usr/bin/python
#coding=utf8

from stockK import stockK
from handleData import tools
from datetime import datetime
import sys
import threading

def dayWork(data):
    stockArray = [stockK("399001"),stockK("002273")]
    for stock in stockArray:
        printInfo(stock)
        
def SixtyMinWork():
    stock60 = stockK(code = '399001',ktype = '60')
    printInfo(stock60)

def thirtyMinWork():
    stock30 = stockK(code = '399001',ktype = '30')
    printInfo(stock30)

def printInfo(stock):
    print(datetime.now())
    print(stock.code)
#     print stock.getHistWithValueType(type = 'high')
    print(stock.K())
    print(stock.D())
    print(stock.kdStatus())
    print(stock.BOLL())
    
def printKInfo():
    stock = stockK(code='399001',ktype='30')
    print(stock.listArray)

    
def thread1():
    tools.scheWithTrigger(name = SixtyMinWork ,second='10,30')

def thread2():
    tools.scheWithTrigger(name = thirtyMinWork ,second='20,40')
    
if __name__ == "__main__":
    SixtyMinWork()
#     print 'start thread'
#     threads = []
#     t1 = threading.Thread(target=thread1)
#     threads.append(t1)
#     t2 = threading.Thread(target=thread2)
#     threads.append(t2)

#     for t in threads:
#         t.start()


#     tools.scheWithTrigger(name = thirtyMinWork,hour='9-11,13-15',
#                  minute='01,31')
#     
#     tools.scheWithTrigger(name = SixtyMinWork,hour='9-11,13-15',
#                 minute='31')
    