# -*- coding: utf-8 -*-

# 原则：
# 1、只做固定几只股票，其他股票判断市场情绪
# 2、

# 策略
# 1、量能萎缩

def lnws(v,v_ma,p=40):
    return (v/v_ma < p/100)

