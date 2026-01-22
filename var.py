
# -------------------------- Find Historical VaR Using Formulas --------------------------
def historical_var(portfolio_returns, alpha):
    sorted_returns = portfolio_returns.sort_values()
    var_value = sorted_returns.quantile(alpha)
    return var_value

# -------------------------- Find Historical CVaR using VaR --------------------------
def historical_cvar(portfolio_returns, alpha):
    sorted_returns = portfolio_returns.sort_values()
    var_value = historical_var(portfolio_returns, alpha)
    tail_losses = portfolio_returns[portfolio_returns <= var_value]
    cvar_value = tail_losses.mean()
    return cvar_value