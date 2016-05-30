import tushare as ts
import time

def getDataWithArray(codeArr):
    while True:
        df = ts.get_realtime_quotes(codeArr)
#pandas    
        gfb = df[['name','pre_close','price','time']]
#     print(ts.get_index())
        print(gfb)
        time.sleep(5)
    
if __name__ == '__main__':
    getDataWithArray(['399001','150206','399973'])