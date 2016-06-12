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
    
    def __init__(self, code , ktype='D'):
        self.code = code
        self.ktype = ktype
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
        return round(self.kValue,2)
    
    def D(self,M2=3,N=9,ref=0):
        KArray = []
        for i in range(0,M2):
            k = self.K(3, 9, i)
            KArray.append(k)
        return round(tools.SMA(KArray, 1),2)

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
        dataArrayC = self.getHistWithValueType('close')[0:20]
        print len(dataArrayC)
        boll=round(tools.MA(dataArrayC),2)
        std = np.std(dataArrayC)
        ub = round(boll + 2*std,2)
        lb = round(boll - 2*std,2)
        bollStatus =  round((ub-lb)/boll,3)
        close = dataArrayC[0]
        closeStatus = round((close - lb)/(ub-lb),2)
#         cb = (close-boll) >= 0 
#         if cb:
#             bstatus = (c-boll)/(ub-boll)
#         else :
#             bstatus = (c-boll)/(boll-lb)
#         需要计算以下状态
#         1.价格在boll位置
#         2.boll中轨朝向
#         10295 9495
        return {'boll':boll,'ub' : ub,'lb':lb,'bollStatus' : bollStatus,'closeStatus':closeStatus}
#         return "close = %s ,boll = %s ,ub = %s ,lb = %s,ulstatus = %s ,bstatus = %s"%(dataArrayC[0],boll,ub,lb,ulstatus,bstatus)
        
    def getHistData(self,N=20):
#         print '需要获取周期：%s，取得周期%s' % (ktype, N)
        df = ts.get_hist_data(self.code,start='2016-05-02',ktype=self.ktype)
        self.listArray = df
        
        
    def getHistWithValueType(self, type ='close'):
#         open   high  close    low     volume  price_change  p_change 
#         ma5    ma10    ma20      v_ma5     v_ma10     v_ma20  turnover     
        return tools.dataFrameToArray(self.listArray[[type]].values)
        