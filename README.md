# Sector ETF Performance Analysis (2020–2025)

A clean, modular Python project that analyzes the risk-return profile of major US market sectors using real ETF data from Yahoo Finance.

## Project Overview
This project:
- Downloads adjusted close prices for 10 major sector ETFs
- Calculates annualized returns and volatility
- Computes sector correlation matrix
- Visualizes:
  - Price trends over time
  - Volatility ranking
  - Correlation heatmap
  - Risk vs Return scatter plot

## Sector ETFs Used
| Sector                | ETF Ticker | Name                          |
|-----------------------|------------|-------------------------------|
| Technology            | XLK        | Technology Select Sector SPDR |
| Healthcare            | XLV        | Health Care Select Sector     |
| Financials            | XLF        | Financial Select Sector       |
| Consumer Discretionary| XLY        | Consumer Discretionary SPDR   |
| Consumer Staples      | XLP        | Consumer Staples SPDR         |
| Energy                | XLE        | Energy Select Sector          |
| Industrials           | XLI        | Industrial Select Sector      |
| Utilities             | XLU        | Utilities Select Sector       |
| Materials             | XLB        | Materials Select Sector       |
| Real Estate           | XLRE       | Real Estate Select Sector     |

## Requirements
- Python 3.8+
- See `requirements.txt`



## Installation & Setup
```bash
git clone https://github.com/saragheisar9-blip/Market_pulse.git
cd sector-etf-analysis
pip install -r requirements.txt
```

## Start Project
```bash
python src/main.py
```