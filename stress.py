scenarios = {
    "market_crash": -0.2,          
    "rate_spike": -0.05,           
    "volatility_spike": -0.1,      
    "tech_boom": 0.15,             
    "market_rally": 0.1             
}


def apply_stress(portfolio_returns, scenario):
    shock = scenarios[scenario]
    stressed_returns = portfolio_returns * (1+shock)
    return stressed_returns