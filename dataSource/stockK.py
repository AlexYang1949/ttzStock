#!/usr/bin/python
#coding=utf8
'''
Created on 2016年5月31日

@author: shunweiwuxian
'''
from handleData import tools
import numpy as np


import tushare as ts
from pycparser.c_ast import Switch
from pip._vendor.distlib._backport.tarfile import TUREAD
from blaze.expr.reductions import std

class stockK(object):
    '''
    根据code创建一个对象
    '''
    
    def __init__(self, code):
        self.code = code
        
    def K(self,M1=3,N=9,ref=0):
        dataArrayC = self.getHistData(N,'D','C')[ref:N+ref]
        dataArrayH = self.getHistData(N,'D','H')
        dataArrayL = self.getHistData(N,'D','L')
        rsaArray = []
        for i in range(0,M1):
            close = dataArrayC[i+ref]
            llv = tools.LLV(dataArrayL[i+ref:N+ref+i])
            hhv = tools.HHV(dataArrayH[i+ref:N+ref+i])
            rsa=(close-llv)/(hhv-llv)*100;                         
            rsaArray.append(rsa)
        return tools.SMA(rsaArray, 1)
    
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
        if ((self.K(ref=ref)>self.D(ref=ref)) & (self.K(ref=ref)>self.K(ref=ref+1))):
            KDYD = True
        if ((self.K(ref=ref)<self.D(ref=ref)) & (self.K(ref=ref)<self.K(ref=ref+1))):
            KYYD= True
        if self.K(ref=ref)>self.K(ref=ref+1):
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

        
    def getHistData(self,N=20,ktype='D', value = 'C'):
#         print '需要获取周期：%s，取得周期%s' % (ktype, N)
        df = ts.get_hist_data(self.code,start='2016-05-02',ktype=ktype)
        if value =='C':
             return tools.dataFrameToArray(df[['close']].values)
        if value =='H':
            return tools.dataFrameToArray(df[['high']].values)
        if value == 'L':
            return tools.dataFrameToArray(df[['low']].values)
        else:
            return None
        