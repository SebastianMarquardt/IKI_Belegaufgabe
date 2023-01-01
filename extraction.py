import yfinance as yf
import pandas as pd


def get_and_save_data(ticker: str, period: str = 'ytd', interval: str = '1d') -> pd.DataFrame:
    # Get all Data
    data = yf.Ticker(ticker)
    # Get only historic Data
    hist = data.history(period=period, interval=interval, rounding=True)
    # Adds Bernoulli-Trends to the Data
    hist = add_up_down_movement(hist)
    # Save Dataframe to .csv and return it
    hist.to_csv(f"OHLCV_{ticker}_{period}_{interval}.csv")
    return hist


def add_up_down_movement(hist_data: pd.DataFrame):
    # Drop unnecessary columns
    hist_data.drop(['High', 'Low', 'Volume', 'Dividends', 'Stock Splits'], axis=1, inplace=True)
    # Calculate absolute change and percentage during each time period
    hist_data['diff'] = hist_data['Close'] - hist_data['Open']
    hist_data['percentage_change'] = (hist_data['Close'] - hist_data['Open']) / hist_data['Open'] * 100

    # Calculate Opening Trend in each period (compare "Open" at t(n) to "Open" at t(n-1))
    hist_data['trend_open'] = hist_data['Open'].rolling(2).apply(diff)
    hist_data['trend_open'] = hist_data.apply(lambda row: add_trend_to_row(row, 'trend_open'), axis=1)

    # Calculate Closing Trend in each period (compare "Close" at t(n) to "Close" at t(n-1))
    hist_data['trend_close'] = hist_data['Close'].rolling(2).apply(diff)
    hist_data['trend_close'] = hist_data.apply(lambda row: add_trend_to_row(row, 'trend_close'), axis=1)
    return hist_data


def add_trend_to_row(row: pd.Series, col_name: str) -> str:
    # Helper function to apply labels
    if row[col_name] < 0:
        return 'down'
    else:
        return 'up'


def diff(x):
    # Helper function to find difference of 2 fields in 1 row
    d = x.iloc[1] - x.iloc[0]
    return d
