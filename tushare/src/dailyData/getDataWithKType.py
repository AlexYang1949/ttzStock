#!/usr/bin/python
#coding=utf-8
import tushare as ts

def getStockKInfo(codeArr):
    df = ts.get_hist_data('399001',start='2016-05-18',ktype='30')
#     gfb = df[['open','close']]
#     print(ts.get_index())
    print(df)

if __name__ == '__main__':
    getStockKInfo(['399001','150206','399973'])