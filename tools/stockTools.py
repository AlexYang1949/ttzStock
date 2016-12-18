# -*- coding: utf-8 -*-

class stockTools(object):
    @classmethod
    def func(cls):
        print('im a classmethod!')

    @classmethod
    def func2(cls):
        print('func2')

    # 获取n天前的成交量
    def refV(cls,n):
