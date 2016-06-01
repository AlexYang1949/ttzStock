#!/usr/bin/python
#coding=utf8

from stockK import stockK

def printInfo():
#     stock = stockK("399001")
    stock = stockK("002273")
#     68 57
    print stock.getHistWithValueType(type = 'high')
    print stock.K()
    print stock.D()
    print stock.kdStatus()
    
if __name__ == "__main__":
    printInfo()
    