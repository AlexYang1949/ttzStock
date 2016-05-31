#!/usr/bin/python
#coding=utf8

from stockK import stockK

def printInfo():
    stock = stockK("399001")
#     68 57
    print stock.K(ref=1)
    print stock.D(ref=1)
    print stock.status(ref=1)
    
if __name__ == "__main__":
    printInfo()
    