#coding=utf-8
import pandas as pd
import tushare as ts
from sqlalchemy import create_engine
import time
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def printDemo():
    s = pd.Series([1,2,3,4,5])
    s.plot()
    print('dataFrame')
    
def printDataFrame():
    dates = pd.date_range('2015-04-05', periods = 6)
    df = pd.DataFrame(np.random.randn(6,4), index = dates ,columns = list(['A','B','C','D']))
    return df
#     print(df)

def insertDB(df):
#     df = ts.get_tick_data('600848', date='2014-12-22')
#     engine = create_engine('mysql://user:passwd@127.0.0.1/db_name?charset=utf8')
#     #存入数据库
#     df.to_sql('tick_data',engine)
    print( df)
    
def realTime(code):
    df = ts.get_realtime_quotes(code)
    printInfo = df[['name','pre_close','price','amount']]
    print(printInfo)
    
def bigRealTime(code):
    df = ts.get_sina_dd(code = code,date = '2016-05-17')
    print(df)

def lhb():
    lhn = ts.top_list('2016-05-16')
    lhc = ts.cap_tops()
    print(lhc)
    
if __name__ == '__main__':
    insertDB(printDataFrame())
#     while True:
#         realTime('399973')
#         time.sleep(3)
    
    