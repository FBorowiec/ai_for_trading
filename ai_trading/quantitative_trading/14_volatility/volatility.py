import pandas as pd
import numpy as np


def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.

    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']

    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    price_data = prices.reset_index().pivot(
        index="date", columns="ticker", values="price"
    )

    # calculating the log returns
    log_return = np.log(price_data) - np.log(price_data.shift(1))

    # calculating the standard deviation and returning the ticker with the highest
    return np.std(log_return).idxmax()


def test_run(filename="ai_trading/quantitative_trading/14_volatility/prices.csv"):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=["date"])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == "__main__":
    test_run()
