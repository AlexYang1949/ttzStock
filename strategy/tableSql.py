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
engine = create_engine('mysql://%s:%s@%s:%d/%s?charset=utf8' % (config['user'], config['password'], config['host'], config['port'],
                                                   config['db']))
con = engine.connect()
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# dbc = con.connection.cursor()
# con.set_character_set('utf8')
# dbc.execute('SET NAMES utf8;')
# dbc.execute('SET CHARACTER SET utf8;')
# dbc.execute('SET character_set_connection=utf8;')
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

def test_all_stock_info():
    # 获取所有的股票
    today_all = ts.get_today_all()
    # print(today_all)
    with con:
        # .drop(['name'], axis=1)
        # today_all['name'].apply(lambda name: name.encode('utf-8').decode('utf-8'))
        # print(today_all['name'])
        today_all.to_sql(name='today_all',con=con,if_exists='append',index=True,index_label='num')
        df = pd.read_sql('select * from today_all;', con=con)
        print(df)
        # print(df.index,df.columns)

def test_stock_info(code):
    # 获取股票
    stock_info = ts.get_hist_data(code=code)
    if stock_info is None:
        return
    con = engine.connect()
    with con:
        print(code+'开始存储')
        stock_info['code']=code
        stock_info.to_sql(name='stock_info',con=con,if_exists='append',index=True)
        print(code+'存储成功')
        # print(df.index,df.columns)

def get_table_data(name):
    with con:
        # print(con.connection.cursor().execute('select name from today_all;'))
        df = pd.read_sql('select * from %s WHERE num>152;'%name, con=con)
        # df = pd.read_sql('select * from %s where code=603188;'%name, con=con)
        for code in df['code']:
            test_stock_info(code)


def test_zz500s():
    df = ts.get_zz500s()
    print(df.index())

def test_pandas():
    pass

def test_plot():
    pass

if __name__ == '__main__':
    # df = pd.read_sql('select * from today_all;', con=con)
    # print(df)
    # test_all_stock_info()
    # test_stock_info('600345')
    get_table_data('today_all')
    # df = pd.read_sql('select * from stock_info;' , con=con)
    # print(df)