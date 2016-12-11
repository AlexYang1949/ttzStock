#!/usr/bin/python
# -*- coding: utf-8 -*-

import tushare as ts
import pymysql
import pandas as pd

# Obtain a database connection to the MySQL instance
config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'test1'
}

engine = pymysql.connect(**config)

def info(data):
	print('type=%s,value=%s'%(data.__class__,data))

def stockCodes():
	hs300 = ts.get_hs300s()
	hs300CodeArr = []
	for hs300Code in hs300.values:
		info(hs300Code)
		hs300CodeArr.append(hs300Code[0])
	# info(hs300CodeArr)

def stock_h_data():
	stock_h = ts.get_hist_data('600318')
	insert_dataFrame_data(stock_h)

def insert_dataFrame_data(data):
	data.to_sql('hs300',engine,if_exists='append')
	# df = pd.read_sql('hs300',engine)
	print(df)

def insert_daily_data_into_db(daily_data):
    """
    Takes a list of tuples of daily data and adds it to the
    MySQL database. Appends the vendor ID and symbol ID to the data.

    daily_data: List of tuples of the OHLC data (with 
    adj_close and volume)
    """
    # Create the time now
    now = datetime.datetime.utcnow()

    # Amend the data to include the vendor ID and symbol ID
    daily_data = [
        (data_vendor_id, symbol_id, d[0], now, now,
        d[1], d[2], d[3], d[4], d[5], d[6]) 
        for d in daily_data
    ]

    # Create the insert strings
    column_str = """code, name, data, open, 
                 high, close, low, volume, 
                 price_change, p_change, ma5,
                 ma10, ma20, v_ma5, v_ma10, v_ma20, turnover"""
    insert_str = ("%s, " * 11)[:-2]
    final_str = "INSERT INTO hs300 (%s) VALUES (%s)" % \
        (column_str, insert_str)
    print('insert_str = '+insert_str+'final_str')
    # Using the MySQL connection, carry out an INSERT INTO for every symbol
    with con: 
        cur = con.cursor()
        # cur.executemany(final_str, daily_data)

if __name__ == '__main__':
	stock_h_data()