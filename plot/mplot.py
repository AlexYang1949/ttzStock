# -*- coding:utf-8 -*-
from matplotlib.ticker import Formatter
from  handleData import tableSql
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY,date2num
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc

class Plot():
    def __init__(self):
        pass

    @staticmethod
    def plotWithDF():
        print('plotWithDF')

    def getData(self,code):
        df = tableSql.excuteSql('select * from stock_info where code=%s;'%code)
        return df

    def plotK(self,df,title='',fmt='%Y-%m-%d'):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        mondays = WeekdayLocator(MONDAY)  # major ticks on the mondays
        alldays = DayLocator()  # minor ticks on the days
        weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
        dayFormatter = DateFormatter('%d')  # e.g., 12

        dataArray= [[date2num(rev.date),rev['open'],rev['high'],rev['low'], rev['close']] for index, rev in df[:50].iterrows()]
        print(dataArray)
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        # ax.xaxis.set_major_locator(mondays)
        # ax.xaxis.set_minor_locator(alldays)
        # ax.xaxis.set_major_formatter(weekFormatter)
        # ax.xaxis.set_minor_formatter(dayFormatter)

        # plot_day_summary(ax, quotes, ticksize=3)
        candlestick_ohlc(ax, dataArray, width=0.6)

        # ax.xaxis_date()
        ax.autoscale_view()
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

        plt.title(title)
        plt.show()


if __name__ == '__main__':
    pl = Plot()
    pl.plotK(pl.getData('300166'),title='东方国信 300166')