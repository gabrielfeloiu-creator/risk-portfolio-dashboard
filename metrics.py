import numpy as np

def sharpe_ratio(portfolio_returns, risk_free_rate=0.0):
    mean_return = np.mean(portfolio_returns)
    volatility = np.std(portfolio_returns)
    if volatility == 0:
        return np.nan
    return (mean_return - risk_free_rate) / volatility
def max_drawdown(portfolio_returns):
    cum_returns = portfolio_returns.cumsum()
    running_max = cum_returns.cummax()
    drawdowns = cum_returns - running_max
    max_dd = drawdowns.min()

    return max_dd