import numpy as np
import pandas as pd
import yfinance as yf

# -------------------------- Load Prices In --------------------------
def load_prices(tickers, start_date, end_date):
    
    # Use auto_adjust=True to ensure we get adjusted prices in the 'Close' column
    data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)
    
    if data.empty:
        raise ValueError("No data found for the given tickers and date range.")

    if isinstance(data.columns, pd.MultiIndex):
        price_df = data['Close']
    else:
        price_df = data[['Close']]
        price_df.columns = [tickers[0]] if isinstance(tickers, list) else [tickers]

    return price_df
# -------------------------- Load the Portfolio, Ensure Weight Sum --------------------------
def load_portfolio(file_path):
    portfolio_df = pd.read_csv(file_path)
    sum_weights = sum(portfolio_df['weight'])
    if round(sum_weights, 6) != 1:
        print("Warning: Weights do not sum to 1")
    return portfolio_df
