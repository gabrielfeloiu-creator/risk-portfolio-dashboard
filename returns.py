import pandas as pd
import numpy as np

# -------------------------- Compute Returns Using Numpy --------------------------
def compute_returns(price_df, method = "log"):
    shifted_price = price_df.shift(1)
    if method == "log":
        price = np.log(price_df / shifted_price)
    else:
        price = (price_df - shifted_price) / shifted_price
    price = price.dropna()
    return price