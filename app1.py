# app1.py
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

from data.loader import load_prices, load_portfolio
from risk.returns import compute_returns
from analytics.portfolio import compute_portfolio_returns
from risk.var import historical_var, historical_cvar
from risk.stress import apply_stress, scenarios
from analytics.metrics import sharpe_ratio, max_drawdown
from plots import plot_equity_curve, plot_pnl_distribution

st.set_page_config(page_title="Portfolio Risk Dashboard", layout="wide")

st.title("Portfolio Risk Dashboard")
st.sidebar.header("Data Settings")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-12-31"))
# --- Upload portfolio CSV ---
uploaded_file = st.file_uploader("Upload portfolio CSV", type="csv")
if uploaded_file is not None:
    # 1. Load the portfolio info
    portfolio_df = pd.read_csv(uploaded_file)
    tickers = list(portfolio_df['asset'])
    weights_series = portfolio_df.set_index('asset')['weight']

    # 2. Use the cleaned-up loader (Dates come from sidebar inputs)
    price_df = load_prices(tickers, start_date=start_date, end_date=end_date)
    
    # 3. Proceed with returns
    returns_df = compute_returns(price_df, method="log")

    # Optional: save to CSV
    price_df.to_csv("all_prices.csv")
    weights_series = portfolio_df.set_index('asset')['weight']

    # --- Load price data ---
    

    price_df = load_prices(tickers, start_date=start_date, end_date=end_date)

    # --- Compute returns ---
    returns_df = compute_returns(price_df, method="log")
    portfolio_returns = compute_portfolio_returns(returns_df, weights_series)

    # --- Metrics ---
    st.sidebar.header("Risk Metrics")
    risk_free_rate = st.sidebar.number_input("Risk-Free Rate", value=0.02)
    alpha = st.sidebar.slider("VaR / CVaR alpha", min_value=0.01, max_value=0.2, value=0.05)

    sharpe = sharpe_ratio(portfolio_returns, risk_free_rate=risk_free_rate)
    max_dd = max_drawdown(portfolio_returns)
    var = historical_var(portfolio_returns, alpha)
    cvar = historical_cvar(portfolio_returns, alpha)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Sharpe Ratio", f"{sharpe:.2f}")
    col2.metric("Max Drawdown", f"{max_dd:.2%}")
    col3.metric(f"VaR ({int(alpha*100)}%)", f"{var:.2%}")
    col4.metric(f"CVaR ({int(alpha*100)}%)", f"{cvar:.2%}")

    # --- Stress test ---
    st.sidebar.header("Stress Test")
    scenario_choice = st.sidebar.selectbox("Select Scenario", list(scenarios.keys()))
    stressed_returns = apply_stress(portfolio_returns, scenario_choice)
    st.write(f"Stressed Portfolio Returns: {scenario_choice}")

    # --- Plots ---
    st.subheader(f"Equity Curve - {scenario_choice} Scenario")
    # Note: We pass STRESSED_RETURNS here so the graph updates!
    plot_equity_curve(stressed_returns, show_in_streamlit=True)

    st.subheader("Normal Distribution (Base Portfolio)")
    plot_pnl_distribution(portfolio_returns, var=var, cvar=cvar, show_in_streamlit=True)

    # --- Download returns ---
    st.download_button(
        label="Download Portfolio Returns",
        data=portfolio_returns.to_csv().encode("utf-8"),
        file_name="portfolio_returns.csv",
        mime="text/csv"
    )
else:
    st.info("Upload a portfolio CSV to get started.")
