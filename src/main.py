import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import functions from custom modules
from data_handler import download_sector_data
from analysis_engine import calculate_financial_metrics

# ----------- Sector ETF Tickers -------------
sectors = {
'Technology': 'XLK',
'Healthcare': 'XLV',
'Financials': 'XLF',
'Consumer Discretionary': 'XLY',
'Consumer Staples': 'XLP',
'Energy': 'XLE',
'Industrials': 'XLI',
'Utilities': 'XLU',
'Materials': 'XLB',
'Real Estate': 'XLRE'
}

# ----------- Date Range -------------
start_date = "2020-01-01"
end_date = "2025-01-01"


# --- Execution Flow ---

# 1. Download and Prepare Data
try:
    data = download_sector_data(sectors, start_date, end_date)
except RuntimeError as e:
    print(e)
    exit()

# 2. Calculate Metrics
annual_returns, volatility, correlation, returns = calculate_financial_metrics(data)


# 3. Visualisation

def plot_sector_prices(data: pd.DataFrame):
    """Generates a line plot of sector ETF prices over time."""
    plt.figure(figsize=(14, 6))
    for col in data.columns:
        plt.plot(data.index, data[col], label=col)
    plt.title("Sector ETF Prices (Normalized to 100 for better comparison)")
    plt.xlabel("Date")
    plt.ylabel("Price Index") # Note: You might want to normalize prices for better comparison if desired
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def plot_volatility(volatility: pd.Series):
    """Generates a bar chart of annualized volatility by sector."""
    plt.figure(figsize=(10, 6))
    volatility.sort_values(ascending=False).plot(kind="bar", color='skyblue')
    plt.title("Annualized Volatility by Sector")
    plt.ylabel("Volatility (Standard Deviation)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(correlation: pd.DataFrame):
    """Generates a heatmap of the sector correlation matrix."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Sector Correlation Matrix")
    plt.tight_layout()
    plt.show()

def plot_risk_vs_return(annual_returns: pd.Series, volatility: pd.Series):
    """Generates a scatter plot comparing annualized risk and return."""
    plt.figure(figsize=(12, 7))
    plt.scatter(annual_returns, volatility, s=200, alpha=0.7, edgecolors='w')

    for sector in annual_returns.index:
        plt.text(
            annual_returns[sector] * 1.02, # Offset X slightly
            volatility[sector],
            sector,
            fontsize=10,
            ha="left",
            va="center"
        )

    plt.xlabel("Annualized Return (Higher is Better)")
    plt.ylabel("Annualized Volatility (Risk) (Lower is Better)")
    plt.title("Risk vs Return of Market Sectors")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Run the plots
plot_sector_prices(data)
plot_volatility(volatility)
plot_correlation_heatmap(correlation)
plot_risk_vs_return(annual_returns, volatility)

print("\n--- Project Execution Complete ---")