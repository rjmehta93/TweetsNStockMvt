#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:36:50 2017

@author: Taranpreet singh

Importing Financial data in python using 'pandas_datareader' library


"""
# to install library use Terminal 'pip install pandas_datareader'

#importing libraries

import matplotlib.pyplot as plt
from pandas_datareader.data import DataReader
# date time to use date objects
from datetime import date

# Time period of import, start and end dates 
start = date(2017,10,01)
end = date(2017,11,06)


# DataReader is a function to import, there are different sources available to import data
# such as ggogle fin, yahoo fin,fred, Oanda(for exchange rates)

# for eg Importing FB data from goolge
stockFb = DataReader('fb', 'google', start, end)
type(stockFb)
# DataReader returns a pandas data frame object

stockFb.head()
stockFb.info()

# from yahoo
stockApl = DataReader('AAPL', 'yahoo', start, end)
stockApl.head()
stockApl.info()

#plotting
stockApl['Close'].plot(title='APPLE')
plt.show()


#sp500 from fred up to now
sp500=DataReader('SP500', 'fred', start)
#note sys date is deafult for end argument
sp500.tail()
sp500.plot(title='SP500')

#saving locally
sp500.to_csv('SP500')
