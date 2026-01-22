import pandas as pd
import numpy as np


# -------------------------- Computing Portfolio Returns --------------------------
def compute_portfolio_returns(returns_dataframe, weights):
    portfolio_returns = (returns_dataframe * weights).sum(axis=1)
    missing_assets = set(returns_dataframe.columns) - set(weights.index)
    if missing_assets:
        raise ValueError ("Missing weights for some assets: " + list [missing_assets])

    return portfolio_returns