import tushare as ts

def init():
# 10493c8248a604a7e07c7d761308f92ad5d662d404e4d43fe3af27f4c65edfe8
    token = '10493c8248a604a7e07c7d761308f92ad5d662d404e4d43fe3af27f4c65edfe8'
    ts.set_token(token)

def futureInfo():
    fd = ts.Future()
    df = fd.Futu(exchangeCD='CCFX', field='secShortName,contractObject,minChgPriceNum,lastTradeDate,deliMethod')
    print(df)
    
if __name__ == '__main__':
    init()
    futureInfo()
    