# -*- coding: utf-8 -*-

from tools.stockTools import stockTools
from strategy_model import short_strategy

if __name__=='__main__':
    print(short_strategy.lnws(200,400))

# 满足5天上涨10%，的起涨点的KD、量能、ma20均线偏离等
# 