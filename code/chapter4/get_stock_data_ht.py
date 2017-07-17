import tushare as ts

df = ts.get_hist_data('601688',start='2013-01-05',end='2017-01-09')

df.to_csv('dataht.csv',columns=['open','high','low','close','volume'])