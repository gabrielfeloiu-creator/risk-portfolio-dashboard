# plots.py
import matplotlib.pyplot as plt
import streamlit as st

def plot_pnl_distribution(portfolio_returns, var=None, cvar=None, show_in_streamlit=False):
    # Create a fresh figure and axis object
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.hist(portfolio_returns, bins=50, color="skyblue", edgecolor="black", alpha=0.7)
    
    if var is not None:
        ax.axvline(x=var, color='orange', linestyle='--', label=f"VaR: {var:.2%}")
    if cvar is not None:
        ax.axvline(x=cvar, color='red', linestyle='--', label=f"CVaR: {cvar:.2%}")
    
    ax.set_title("Portfolio Returns Distribution")
    ax.set_xlabel("Returns")
    ax.set_ylabel("Frequency")
    ax.grid(True)
    ax.legend()

    if show_in_streamlit:
        st.pyplot(fig)  # Pass the specific figure object
        plt.close(fig)  # Clean up memory
    else:
        plt.show()

def plot_equity_curve(portfolio_returns, show_in_streamlit=False):
    # Create a fresh figure and axis object
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Using cumprod is usually more accurate for finance than cumsum
    # (1 + r).cumprod() accounts for compounding
    cum_returns = (1 + portfolio_returns).cumprod()
    
    ax.plot(cum_returns, color='blue')
    ax.set_title("Equity Curve (Compounded)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value")
    ax.grid(True)

    if show_in_streamlit:
        st.pyplot(fig)  # Pass the specific figure object
        plt.close(fig)  # Clean up memory
    else:
        plt.show()