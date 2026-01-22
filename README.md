# Portfolio Risk Dashboard

Interactive Python app for analyzing portfolio risk and performance using historical returns, Value-at-Risk (VaR), Conditional VaR (CVaR), stress testing, and key financial metrics.

## Features
- Upload custom portfolio CSV with asset weights
- Compute portfolio returns using log returns
- Risk metrics: Sharpe Ratio, Max Drawdown, VaR, CVaR
- Stress testing with predefined market scenarios
- Visualizations: equity curves and P&L distributions
- Download computed portfolio returns

## Key Assumptions
- Portfolio returns are computed as a weighted sum of individual asset log returns
- Historical returns are used to compute VaR and CVaR
- Stress scenarios are predefined and applied to portfolio returns
- Risk-free rate is constant over the analyzed period

## Tech Stack
Python, NumPy, Pandas, Streamlit, Matplotlib, yfinance

## Run
```bash
pip install -r requirements.txt
streamlit run app1.py
