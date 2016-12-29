#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import tushare as ts
import pandas as pd
import time

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'test1'
}
# con = pymysql.connect(**config)
# 初始化数据库连接:
engine = create_engine('mysql://%s:%s@%s:%d/%s' % (config['user'], config['password'], config['host'], config['port'],
                                                   config['db']))

con = engine.connect()
# create_table_sql = 'CREATE TABLE `hs300`( \
#                 `date` datetime NOT NULL , \
#                 `code` varchar(32) NOT NULL,\
#                 `open` decimal(19,4) NULL,\
#                 `close` decimal(19,4) NULL,\
#                 `low` decimal(19,4) NULL,\
#                 `volume` bigint NULL,\
#                 `price_change` decimal(19,4) NULL,\
#                 `p_change` decimal(19,4) NULL,\
#                 PRIMARY KEY (`date`)\
# )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;'
con = engine.connect()

# create_table_sql = 'CREATE TABLE `hs300`( \
#                     `date` datetime NOT NULL , \
#                     `code` varchar(32) NOT NULL,\
#                     `open` decimal(19,4) NULL,\
#                     `low` decimal(19,4) NULL,\
#                     `volume` bigint NULL,\
#                     `price_change` decimal(19,4) NULL,\
#                     `p_change` decimal(19,4) NULL,\
#
#                     PRIMARY KEY (`date`)\
#
# )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;'

select_sql = 'select *from hs300;'
delete_sql = 'delete from hs300 where 1=1;'


# def insertData(code,)

def test_insert():
    with con:
        cur = con.connection.cursor()
        print('网络请求开始')
        print(time.strftime("%H:%M:%S", time.localtime()))
        data1 = ts.get_hist_data(code='300126')
        print(data1.keys)
        print(time.strftime("%H:%M:%S", time.localtime()))
        df = pd.read_sql('select * from hs300;', con=con)
        print(time.strftime("%H:%M:%S", time.localtime()))
        # print(df)
        con.close()

def test_stock_info():
    # 获取所有的股票
    today_all = ts.get_today_all()
    with con:
        today_all.to_sql('today_all',con)
        df = pd.read_sql('select * from today_all;', con=con)
        print(df['nmc'])

def test_zz500s():
    df = ts.get_zz500s()
    print(df.index())

def test_pandas():
    pass

def test_plot():
    pass

if __name__ == '__main__':
    test_zz500s()
