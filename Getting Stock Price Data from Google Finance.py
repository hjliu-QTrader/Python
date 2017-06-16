# Successful run with US stocks. I tried using Yahoo Finance as the source but it didn't work, likely because Yahoo has changed its URL for data downloading. I also tried to use the codes below to obtain HKEX stocks but was not successful - turned out that google does not support HKEX after I spent 2 hours researching.... Guess that I have to continue researching...

#Credit 
# * https://www.youtube.com/watch?v=2BrpKpWwT2A

#Dependencies
# * beautifulsoup4
# * pandas
# * pandas_datareader
# * matplotlib
# * datetime
#Use "sudo -H" which will prompts for password to obtain admin right to install 

#Code Start

import datetime as dt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2017,6,1)
end = dt.datetime(2017,6,12)

df = web.DataReader('BABA','google',start,end) #working fine for US Stocks using stock symbols
print (df.head())


#Code End
