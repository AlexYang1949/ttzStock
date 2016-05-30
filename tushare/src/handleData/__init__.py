#!/usr/bin/python
#coding=utf-8
import tushare as ts
import time
from quotaTool import quota
from handleData import dataFrameTest
# print(ts.get_today_all())
# 399973 150206
# 实时获取数据
def work():
    df = ts.get_realtime_quotes(['399001','150206','399973'])
#pandas    
    gfb = df[['name','pre_close','price','time']]
#     print(ts.get_index())
    print(gfb)
#     col = gfb.get_values()
#     for i:
#     rate = col[]
#     print(col[0][2])

# 1.未成熟随机值（RSV）=（收盘价-N日内最低价）/（N日内最高价-N日内最低价）*100
# 2.K=RSV的M1日移动平均
# 3.D=K的M2日移动平均

def KD(N=3,M1=9,M2=9):
    print('hello KD')
    
if __name__ == '__main__':
    quota.KD()

#     while True:
#         work()
#         time.sleep(5)
    


