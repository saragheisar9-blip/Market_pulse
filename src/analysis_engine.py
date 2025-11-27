import pandas as pd
import numpy as np


def calculate_financial_metrics(data: pd.DataFrame):
    """
    Calculate financial metrics from price data.
    
    Args:
        data: DataFrame with sector names as columns and dates as index
    
    Returns:
        tuple: (annual_returns, volatility, correlation, returns)
            - annual_returns: Series of annualized returns per sector
            - volatility: Series of annualized volatility per sector
            - correlation: DataFrame of correlation matrix between sectors
            - returns: DataFrame of daily returns
    """
    # Compute daily returns
    returns = data.pct_change().dropna()
    
    # Annualized volatility
    volatility = returns.std() * np.sqrt(252)
    
    # Correlation matrix
    correlation = returns.corr()
    
    # Annualized returns
    annual_returns = returns.mean() * 252
    
    return annual_returns, volatility, correlation, returns


