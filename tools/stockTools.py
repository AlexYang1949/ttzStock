# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas_datareader import data
import tushare as ts
import datetime

# import matplotlib.pyplot as plt

# BOLL,MIN,MAX,REF,dayOfIncre,

class stockTools(object):
    # Compute the Bollinger Bands
    @classmethod
    def BBANDS(cls, data, ndays):
        MA = pd.Series(pd.rolling_mean(data['Close'], ndays))
        SD = pd.Series(pd.rolling_std(data['Close'], ndays))
        b1 = MA + (2 * SD)
        B1 = pd.Series(b1, name='Upper BollingerBand')
        data = data.join(B1)

        b2 = MA - (2 * SD)
        B2 = pd.Series(b2, name='Lower BollingerBand')
        data = data.join(B2)
        return data

    @classmethod
    def MIN(cls, dataArr):
        return min(dataArr)

    @classmethod
    def MAX(cls, dataArr):
        return max(dataArr)

    @classmethod
    def REF(cls, dataArr, ndays):
        length = len(dataArr)
        if length > ndays:
            return dataArr[ndays]
        else:
            return not np.nan

    @classmethod
    def MA(cls, dataArr):
        return sum(dataArr)/len(dataArr)

    @classmethod
    def SMA(cls,dataArr, N=10):
        length = len(dataArr)
        return (dataArr[0] * (N + 1) + sum(dataArr[1:length])) / (length + N)

    # n天上涨rate比例
    @classmethod
    def dayOfIncre(cls, data, ndays, rate):
        data = data['close']
        dates = data.index
        closeData = data.values
        length = len(closeData)
        df = pd.DataFrame(columns=('rate', 'beginPrice', 'endPrice', 'date'))
        for index, val in enumerate(closeData):
            if index == length - ndays:
                break
            indexEnd = index
            indexBegin = index + ndays
            beginPrice = closeData[indexBegin]
            endPrice = closeData[indexEnd]
            r = (endPrice - beginPrice) / endPrice
            if r > rate:
                beginDate = dates[indexBegin]
                endDate = dates[indexEnd]
                # print(beginDate.__class__)
                date = "%s----%s" % (beginDate, endDate)
                # print("rate=%s,beginPrice=%s,endPrice=%s,date=%s"%(rate,beginPrice,endPrice,date))
                df.loc[beginDate] = [r, beginPrice, endPrice, date]
        return df

def test():
    pass;

if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    data1 = ts.get_hist_data(code='300126')
    print(data1)
    # print(stockTools.dayOfIncre(data1, 5, 0.1))
    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # print(stockTools.SMA([7,2,3,4,5,6,1]))
    # Retrieve the Nifty data from Yahoo finance:
    # data = data.DataReader('^NSEI', data_source='yahoo', start='1/1/2010', end='1/1/2016')

    # print(data.__class__)
    # df = pd.DataFrame(data)
    # print(data.__class__)
    # print(data)


    # Compute the Bollinger Bands for NIFTY using the 50-day Moving average
    # n = 50
    # NIFTY_BBANDS = stockTools.BBANDS(data, n)
    # print(NIFTY_BBANDS)
    # plt.figure();
    # df.plot();


