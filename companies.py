import yfinance as yf

tickers = yf.Tickers('msft aapl goog')

# access each ticker using (example)
tickers.tickers['MSFT'].info
tickers.tickers['AAPL'].history(period="1mo")
tickers.tickers['DIS'].actions
tickers.tickers['AMZN'].hist 
tickers.tickers['TSLA'].get_info