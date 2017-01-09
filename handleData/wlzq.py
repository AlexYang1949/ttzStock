# -*- coding: utf-8 -*-

# http://www.wlstock.com/ShuJu/StockFundFlow.aspx

from bs4 import BeautifulSoup
from  urllib import request
from plot.mplot import Plot
url = 'http://www.wlstock.com/ShuJu/StockFundFlow.aspx'
with request.urlopen(url) as content:
    print("finish")
    soup = BeautifulSoup(content, 'lxml')
    tbody = soup.tbody

Plot.plotWithDF()
print(soup)