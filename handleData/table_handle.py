#!/usr/bin/python
# -*- coding: utf-8 -*-


import tushare as ts
import pandas as pd
# import matplotlib.pyplot as plt
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

# 初始化数据库连接:
engine = create_engine('mysql://%s:%s@%s:%d/%s?charset=utf8' % (config['user'], config['password'], config['host'], config['port'],
                                                   config['db']))
con = engine.connect()
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
tablename = {'D':'stock_data','30':'stock_30_data'}
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

# 存储大盘数据   sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板
def insert_index_data(code):
    # 获取数据
    index_data = ts.get_hist_data(code=code)
    con = engine.connect()
    with con:
        print(code+'开始存储')
        index_data['code']=code
        index_data.to_sql(name='%s_data'%code,con=con,if_exists='replace',index=True,index_label='date')
        print(code+'存储成功')

# 每日股票数据存储
def insert_all_stock_data():
    # 所有的股票
    today_all = ts.get_today_all()
    # print(today_all)
    with con:
        today_all.to_sql(name='today_all',con=con,if_exists='append',index=True,index_label='num')
        df = pd.read_sql('select * from today_all;', con=con)
        print(df)
        # print(df.index,df.columns)

# ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
def insert_stock_data(code,ktype='D'):
    # 获取股票
    stock_data = ts.get_hist_data(code=code,ktype=ktype)
    if stock_data is None:
        return
    con = engine.connect()
    with con:
        print(code+'开始存储')
        stock_data['code']=code
        stock_data.to_sql(name=tablename[ktype],con=con,if_exists='append',index=True)
        print(code+'存储成功')

def insert_stock_basics_data():
    stock_data = ts.get_stock_basics()
    if stock_data is None:
        return
    con = engine.connect()
    with con:
        stock_data.to_sql(name='stock_basics', con=con, if_exists='append', index=True)
        print('存储成功')


def get_table_data(name):
    with con:
        df = pd.read_sql('select * from %s;'%name, con=con)
        print(df)
        # df = pd.read_sql('select * from %s where code=603188;'%name, con=con)
        # for code in df['code']:
        #     insert_stock_info(code)

def test_pandas():
    pass

def get_base_data():
    df = ts.get_stock_basics()
    print(df)

def plot_data():
    df = pd.read_sql('select close,volume from sh_data;', con=con)
    df['volume'] = df['volume'].apply(lambda v: v / 1500)
    print(df)
    df.plot(kind='line')
    # plt.show()

def excuteSql(sql):
    df = pd.read_sql(sql, con=con)
    return df

if __name__ == '__main__':
    # df = pd.read_sql('select * from today_all;', con=con)
    # print(df)
    # insert_stock_basics_data()
    # insert_stock_data('600345',ktype='30')
    get_table_data(tablename['30'])
    # insert_stock_basics_data()
    # get_table_data()
    # df = excuteSql('select * from stock_basics WHERE pe>0 AND pe<100')
    # for code in df['code']:
    #     insert_stock_data(code,'30')
    # #
    # print('start %s'%time.time())
    # today_all = ts.get_today_all()
    # print('end %s' % time.time())
    # print(today_all)