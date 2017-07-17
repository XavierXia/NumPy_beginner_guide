import tushare as ts

df = ts.get_hist_data('600030',start='2013-01-05',end='2017-01-09')

df.to_csv('datazx.csv',columns=['open','high','low','close','volume'])