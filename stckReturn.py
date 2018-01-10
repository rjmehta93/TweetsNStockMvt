#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:29:14 2017

@author: taranpreet singh
"""

import matplotlib.pyplot as plt
from pandas_datareader.data import DataReader
# date time to use date objects
from datetime import date

# Time period of import, start and end dates 
start = date(2017,10,01)
end = date(2017,11,06)


stockApl = DataReader('AAPL', 'yahoo', start, end)['Close']
stockApl.head()


#plotting
stockApl.plot(title='APPLE')
plt.show()

#calculating daily returns of the stock

dr_apl = stockApl.pct_change(1)

#encoding for comparison
dr_apl[ dr_apl <0 ] = 0   

dr_apl[ dr_apl >0 ] = 4  

#removing Nan
dr_apl=dr_apl[1:]

check['stock']=dr_apl

check=check.dropna()


check['flag'] = np.where(check.sent == check.stock, 1,0) 
#checking corr                               

check.flag.describe()


