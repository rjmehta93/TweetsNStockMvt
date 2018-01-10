#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 20:03:02 2017

@author: TP

My code for importing tweets
"""

import pandas as pd

# works both with python 3.5 and 2.7
import sys
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got



#empty dic to store tweets as items and dates as keys        
tweets={}

#initialising tweet importer 	
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('@UBS').setSince("2016-06-01").setUntil("2016-12-31").setMaxTweets(100)


#Exception handling for cases where tweets are not enough ex QQQ or EOG
#in these cases it will store the max available
try:
#storing results in dic,
   for n in range(9999):
      tweet = got.manager.TweetManager.getTweets(tweetCriteria)[n]
      tweets[tweet.date]=tweet.text
except IndexError:
   print("Not enough tweets, Storing max available")


#print(tweets)
#saving locally
df=pd.DataFrame(tweets.items(), columns=['Date', 'Text'])

#cleaning tweets
replace_reg = "https://t.co/[A-Za-z\\d]+|http://[A-Za-z\\d]+|&amp;|&lt;|&gt;|RT|https"


df.Text=df.Text.str.replace(replace_reg,"")


#print(df)
# encoding for saving twitter special characters
df.to_csv('UBSjun16-dec16.csv',encoding='utf-8')

