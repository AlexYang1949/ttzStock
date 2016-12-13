#!/usr/bin/python
# -*- coding: utf-8 -*-

import tushare as ts
import pymysql
import pandas as pd

# 配置数据库信息
config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'test1'
}

engine = pymysql.connect(**config)

def info(data):
	print('type=%s,value=\n%s'%(data.__class__,data))

def get_hs300_data():
	hs300 = ts.get_hs300s()
	hs300CodeArr = []
	for hs300Code in hs300.values:
		info(hs300Code)
		hs300CodeArr.append(hs300Code[0])
	# info(hs300CodeArr)

def get_stock_data(code):
    stock_h=ts.get_hist_data(code)
    stock_h['code']=code
    insert_dataFrame(stock_h)

def insert_dataFrame(data):
	# data.to_sql(name='hs300',schema='test1',con=engine,if_exists='append')
    column_str = """date, code, open,
                 high, close, low, volume,
                 price_change, p_change"""

    daily_data=[(index,row.code,row.open,row.high,row.close,row.low,row.volume,row.price_change,row.p_change)for index, row in data.iterrows()]
    insert_str = ("%s, " * 9)[:-2]
    final_str = "INSERT INTO hs300 (%s) VALUES (%s)"%\
                (column_str,insert_str)
    print(final_str)
    with engine:
        cur = engine.cursor()
        cur.executemany(final_str,daily_data)

    quary()

def quary():
    select_sql = 'SELECT *FROM hs300'
    cur = engine.cursor()
    cur.execute(select_sql)
    table_data = cur.fetchall()
    for values in table_data:
        info(values)
    # info_arr = []
    # for values in table_data:
    #     length = len(values)
    #     stock_info = []
    #     for i in range(0,length-1):
    #         stock_info.append(values[i])
    #     info_arr.append(stock_info)
    # print(info_arr)
    cur.close()

if __name__ == '__main__':
    # get_stock_data('600318')
    quary()