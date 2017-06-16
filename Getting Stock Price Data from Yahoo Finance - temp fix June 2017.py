#It took me a while to figure out but it worked! Furthermore, to my pleasant surprise, 
#Yahoo Finance supports HKEX data and it requires the format of xxxx.HK.

#Credit
#https://github.com/ranaroussi/fix-yahoo-finance



#Dependencies
#fix_yahoo_finance

#Install at terminal
pip install fix_yahoo_finance --upgrade --no-cache-dir 

#Code Start

import datetime as dt
import fix_yahoo_finance as yf

start = dt.datetime(2017,6,1)
end = dt.datetime(2017,6,12)

df = yf.download([2800.HK',start,end) #working fine for HK Stocks using stock symbols
print (df.head())
#Code End

#More information on the package by the author "ranaroussi"

from pandas_datareader import data as pdr
import fix_yahoo_finance  # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")

# download Panel
data = pdr.get_data_yahoo(["SPY", "IWM"], start="2017-01-01", end="2017-04-30")
data = pdr.get_data_yahoo(
            # tickers list (single tickers accepts a string as well)
            tickers = ["SPY", "IWM", "..."],

            # start date (YYYY-MM-DD / datetime.datetime object)
            # (optional, defaults is 1950-01-01)
            start = "2017-01-01",

            # end date (YYYY-MM-DD / datetime.datetime object)
            # (optional, defaults is Today)
            end = "2017-04-30",#

            # return a multi-index dataframe
            # (optional, default is Panel, which is deprecated)
            as_panel = False,

            # group by ticker (to access via data['SPY'])
            # (optional, default is 'column')
            group_by = 'ticker',

            # adjust all OHLC automatically
            # (optional, default is False)
            auto_adjust = True,

            # download dividend + stock splits data
            # (optional, default is None)
            # options are:
            #   - True (returns history + actions)
            #   - 'only' (actions only)
            actions = True,

            # How may threads to use?
            threads = 10
        )






