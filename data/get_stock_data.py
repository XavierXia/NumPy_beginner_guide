import tushare as ts

df = ts.get_hist_data('000001',start='2013-01-05',end='2017-01-09')

df.to_csv('data.csv',columns=['open','high','low','close','volume'])