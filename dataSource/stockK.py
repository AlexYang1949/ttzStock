#!/usr/bin/python
#coding=utf8
'''
Created on 2016年5月31日

@author: shunweiwuxian
'''
from handleData import tools
import numpy as np
import tushare as ts

class stockK(object):
    '''
    根据code创建一个对象
    '''
    
    def __init__(self, code):
        self.code = code
        self.ktype = 'D'
        self.listArray = None
        self.getHistData()
    
    def K(self,M1=3,N=9,ref=0):
        dataArrayC = self.getHistWithValueType('close')
        dataArrayH = self.getHistWithValueType('high')
        dataArrayL = self.getHistWithValueType('low')
        rsaArray = []
        for i in range(0,M1):
            close = dataArrayC[i+ref]
            llv = tools.LLV(dataArrayL[i+ref:N+ref+i])
            hhv = tools.HHV(dataArrayH[i+ref:N+ref+i])
            rsa=(close-llv)/(hhv-llv)*100;                         
            rsaArray.append(rsa)
        self.kValue = tools.SMA(rsaArray, 1)
        return self.kValue
    
    def D(self,M2=3,N=9,ref=0):
        KArray = []
        for i in range(0,M2):
            k = self.K(3, 9, i)
            KArray.append(k)
        return tools.SMA(KArray, 1)

    def kdStatus(self,ref = 0):
        KDYD = False
        KYYD= False
        BUYTURN = False
        kValue = self.K()
        dValue = self.D()
        if ((kValue>dValue) & (kValue>self.K(ref=ref+1))):
            KDYD = True
        if ((kValue<dValue) & (kValue<self.K(ref=ref+1))):
            KYYD= True
        if kValue>self.K(ref=ref+1):
            BUYTURN = True
        if (BUYTURN == True & KDYD==True):
            return "BUY"
        
        if KYYD == True:
            return 'SELL'
        
        return "TURN"
        
    def BOLL(self,ref=0):
        dataArrayC = self.getHistData()[0:20]
        print len(dataArrayC)
        boll=tools.MA(dataArrayC)
        std = np.std(dataArrayC)
        ub = boll + 2*std
        lb = boll - 2*std
        c = dataArrayC[0]
        status = (c - lb)/(ub-lb)
#         需要计算以下状态
#         1.价格在boll位置
#         2.boll中轨朝向
#         10295 9495
        print "boll = %s ,ub = %s ,lb = %s,status = %s"%(boll,ub,lb,status)

        
    def getHistData(self,N=20):
#         print '需要获取周期：%s，取得周期%s' % (ktype, N)
        df = ts.get_hist_data(self.code,start='2016-05-02',ktype=self.ktype)
        self.listArray = df
        
        
    def getHistWithValueType(self,type ='close'):
#         open   high  close    low     volume  price_change  p_change 
#         ma5    ma10    ma20      v_ma5     v_ma10     v_ma20  turnover 
        return tools.dataFrameToArray(self.listArray[[type]].values)
        