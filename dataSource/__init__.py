#!/usr/bin/python
#coding=utf8

from stockK import stockK
from handleData import tools
def printInfo():

    stockArray = [stockK("399001"),stockK("002273")]
#     stock = stockK("399001")
#     68 57
    for stock in stockArray:
        print stock.code
        print stock.getHistWithValueType(type = 'high')
        print stock.K()
        print stock.D()
        print stock.kdStatus()
    
if __name__ == "__main__":
    tools.scheWithTrigger(name = printInfo, second = '10,20')
    