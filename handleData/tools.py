#!/usr/bin/python
#coding=utf8
'''
Created on 2016年5月31日

@author: shunweiwuxian
'''

def LLV(datas):
    return min(datas)

def HHV(datas):
    return max(datas)

def CROSS(values1=[1,2],values2=[3,4]):
    v10 = values1[0]
    v11 = values1[1]
    v20 = values2[0]
    v21 = values2[1]
    if(v10<v20 & v11>v21):
        print '上穿'
        return True
    else:
        print '没有上穿'
        return False
 
def MA(datas):
    count = 0
    for data in datas:
        count = count + data
    return count/len(datas)

def SMA(datas,N=1):
    length = len(datas)
    ma = MA(datas[1:length])
    return (datas[0]*(N+1) + total(datas[1:length]))/(length+N)
        
def total(datas):
    count = 0
    for data in datas:
        count = count + data
    return count

def dataFrameToArray(datasArray):
    array = []
    for data in datasArray:
        array.append(round(data[0],3))
    return array
    
    
    