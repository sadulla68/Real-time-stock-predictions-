import yfinance as yf

def load_stock(symbol="AAPL", period="2y"):
    df = yf.download(symbol, period=period)
    df.dropna(inplace=True)
    return df
