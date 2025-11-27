import yfinance as yf
import pandas as pd


def download_sector_data(sectors: dict, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Download sector ETF price data from Yahoo Finance.
    
    Args:
        sectors: Dictionary mapping sector names to ticker symbols
        start_date: Start date in 'YYYY-MM-DD' format
        end_date: End date in 'YYYY-MM-DD' format
    
    Returns:
        DataFrame with sector names as columns and dates as index
    
    Raises:
        RuntimeError: If no price data was downloaded
    """
    print("\n--- Downloading Data ---")
    
    tickers = list(sectors.values())
    
    raw = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        group_by="ticker",
        auto_adjust=False,
        progress=False
    )
    
    data = pd.DataFrame()
    
    for sector, ticker in sectors.items():
        print(f"Processing: {ticker} ({sector})")
        try:
            series = raw[ticker]["Adj Close"]
            if series.isna().all():
                print(f"WARNING: No valid Adj Close for {ticker}, skipping.")
                continue
            data[sector] = series
        except Exception as e:
            print(f"ERROR for {ticker}: {e}")
            continue
    
    if data.empty:
        raise RuntimeError("ERROR: No price data was downloaded. Check internet / Yahoo API.")
    
    return data


