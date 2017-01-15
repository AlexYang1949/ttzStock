# -*- coding: utf-8 -*-

import talib as ta
import pandas as pd
import tushare as ts
import numpy as np
import scipy as sp
# import matplotlib as mpl
# import matplotlib.pyplot as plt
import lib.zw_talib as zta

df = None
if df==None:
    df['index'] = ts.get_h_data('600308')
    print(df.index)
    # df = df.sort_values(by=['index'])
    # print(df)

print(zta.BBANDS(df,20))

# def BOLL():
