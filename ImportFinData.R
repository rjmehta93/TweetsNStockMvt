# author - taranpreet
#Importing finacial data
# I am using quantmod package for importing fin data
# installing package, uncomment next line to install
#install.packages("quantmod")


#changing working directory in R
getwd()
#returns current working directory

# use setwd() to change working directory


# Load the quantmod package
library(quantmod)

# Import SPY data from yahoo finance, yahoo is the default source
#getSymbols is a function in quantmod package to import data 
spy<-getSymbols("SPY",auto.assign=FALSE)

# change argument 'src' to import data from different source

#import from google finance

#getSymbols("QQQ",src="google")

# Look at the structure of QQQ
str(spy)
# first six rows
head(spy)

# last six rows
tail(spy)

# getSymbols returns an xts object which is an extensible time series object used 
# in R for storing fin data, zoo is parent class of xts
class(spy)

# so you need to check symbols from the source sites to import data

# Import GDP data from FRED
#FRED is an online database of economic time series data created
# and maintained by the Federal Reserve Bank of St. Louis
gdp <- getSymbols("GDP",src="FRED")

# Look at the structure of GDP
str(gdp)

#data for last 100 days
apple<-getSymbols("AAPL",from = Sys.Date() - 100, to = Sys.Date(),auto.assign=FALSE)
# use from and to import data for specific days


?getSymbols
#to know more about other arguments


#Another option is importing data from Quandl which is a go to site for fin data
# but some datasets are paid

install.packages("Quandl")

library(Quandl)

# Import GDP data from FRED   it works as src/symbol
gdpQ<-Quandl(code="FRED/GDP")

#FRED is source Gdp is symbol
# Look at the structure of the object returned by Quandl
str(gdpQ)
class(gdpQ)
#Quandl() returns a data.frame 


# saving data as csv file locally

write.csv(as.data.frame(apple),"apple100.csv")


#use help(fun) or ?fun if you need to help on any function
# if you are using Rstudio go to help -> cheatsheets for help in R





