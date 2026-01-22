import numpy as np
import pandas as pd
import yfinance as yf

def load_prices(tickers, start_date, end_date):
    """
    Download all tickers at once using yfinance.
    Returns adjusted close prices as a DataFrame.
    """
    # Use auto_adjust=True to ensure we get adjusted prices in the 'Close' column
    data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)
    
    if data.empty:
        raise ValueError("No data found for the given tickers and date range.")

    # With auto_adjust=True, the adjusted price is in 'Close'
    # If downloading multiple tickers, it's a MultiIndex.
    if isinstance(data.columns, pd.MultiIndex):
        price_df = data['Close']
    else:
        # If it's a single ticker, yfinance returns a flat index
        price_df = data[['Close']]
        price_df.columns = [tickers[0]] if isinstance(tickers, list) else [tickers]

    return price_df

def load_portfolio(file_path):
    # (Your existing code remains the same)
    portfolio_df = pd.read_csv(file_path)
    sum_weights = sum(portfolio_df['weight'])
    if round(sum_weights, 6) != 1:
        print("Warning: Weights do not sum to 1")
    return portfolio_df