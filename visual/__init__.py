# -*- coding: utf-8 -*-

from tools.stockTools import stockTools
from strategy_model import short_strategy
from lib import talib_test

if __name__=='__main__':
    talib_test.BOLL()

# 满足5天上涨10%，的起涨点的KD、量能、ma20均线偏离等
# 