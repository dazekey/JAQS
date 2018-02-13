# encoding: utf-8
"""
@author: Ocean_Lane
@contract: dazekey@163.com
@file: test.py
@time: 2018/2/13 23:09
"""
# from __future__ import print_function
# print('good')
# print 'bad'

import pandas as pd

# py 3
from jaqs.data import DataApi  # 导入数据模块

# 登录模块
phone = 13564351621
token = 'quantos85'

api = DataApi(addr='tcp://data.quantos.org:8910')
api.login(phone, token)

# 数据视图DataView
# 初始化 DataView().init_from_config
# DataService提供原始的数据，目前jaqs已经提供远程数据服务类（RemoteDataService），可以通过互联网获取行情数据和参考数据。
from jaqs.data.dataservice import RemoteDataService
from jaqs.data.dataview import DataView
dv = DataView()
ds = RemoteDataService()

secs = '600030.SH,000063.SZ,000001.SZ'
props = {'start_date': 20160601, 'end_date': 20170601, 'symbol': secs,
       'fields': 'open,close,high,low,volume,pb,net_assets,eps_basic',
       'freq': 1}
# dv.init_from_config(props, data_api=ds)  # 初始化 init_from_config

# 数据准备
# dv.prepare_data()
"""jaqs.data.dataservice.NotLoginError: Please first login using init_from_config."""
# snap1 = dv.get_snapshot(20170504, symbol='600030.SH,000063.SZ', fields='close,pb')
# ts1 = dv.get_ts('close', symbol='000001.SH', start_date=20170101, end_date=20170302)
"""AttributeError: 'NoneType' object has no attribute 'loc'"""

# dv.save_dataview('prepared', 'demo')
"""TypeError: save_dataview() takes 2 positional arguments but 3 were given"""

## 日频0/1指标：是否接近涨跌停
# dv.add_formula('limit_reached', 'Abs((open - Delay(close, 1)) / Delay(close, 1)) > 0.095', is_quarterly=False)
# dv.get_ts('limit_reached').iloc[:, 100:].head(2)
"""AttributeError: 'NoneType' object has no attribute 'loc'"""

dataview_props = {# Start and end date of back-test
                  'start_date': 20170101, 'end_date': 20171030,
                  # Investment universe and performance benchmark
                  'universe': UNIVERSE, 'benchmark': '000300.SH',
                  # Data fields that we need
                  'fields': 'total_mv,turnover',
                  # freq = 1 means we use daily data. Please do not change this.
                  'freq': 1}
# RemoteDataService communicates with a remote server to fetch data
# ds = RemoteDataService()
# Use username and password in data_config to login
# ds.init_from_config(data_config)

# DataView utilizes RemoteDataService to get various data and store them
dv = DataView()
dv.init_from_config(dataview_props, ds)
dv.prepare_data()
dv.save_dataview(folder_path=dataview_store_folder)
