# download data from multiple tickers
import yfinance as yf
data = yf.download("companies", start="2017-01-01", end="2017-04-30")


# data
yf.download(tickers = "companies",  # list of tickers
            period = "1y",         # time period
            interval = "1d",       # trading interval
            ignore_tz = True,      # ignore timezone when aligning data from different exchanges?
            prepost = False)       # download pre/post market hours data?