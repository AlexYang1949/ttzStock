#!/usr/bin/python
#coding=utf8

from stockK import stockK

def printInfo():
#     stock = stockK("399001")
    stock = stockK("002273")
#     68 57
#     print stock.K(ref=1)
#     print stock.D(ref=1)
#     print stock.status(ref=1)
    stock123 = stock.getHistData()
    if stock123!=None:
        print 'OK + %s' % len(stock123)
    
if __name__ == "__main__":
    printInfo()
    