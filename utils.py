import jqdatasdk as jq
import pandas as pd
from six import Iterator
import yaml

def jq_login(credentials_file) -> None:
    """Authenticates session for JQData Local API

    Parameters
    -----------
    credentials_file: str
        path to .yml file containing credentials
        requires file to contain entries for 'user:' and 'pass:'
    """
    with open(credentials_file, "r") as stream:
        try:
            credentials = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    jq.auth(credentials["user"], credentials["pass"])
    client = jq.JQDataClient.instance()
    client.ensure_auth()
    assert jq.is_auth()


def get_stock_data(api_func, stocks, *args) -> Iterator:
    """Multi-threaded API-agnostic function for getting stock data
    Parameters
    -----------
    api_func: function
        any api function
    stocks: list
        a list of stock tickers in the format required by your API
    *args:
        0 or more additional arguments for the api_func *by position*
    Returns
    --------
    generator
        a generator object of your API results in the same order as your list of stocks
    """
    MAX_THREADS = 3
    if len(args) > 0:
        api_args = ((stock, *args) for stock in stocks)
    else:
        api_args = ([stock] for stock in stocks)
    #get_current_tick needs to be single threaded
    if api_func.__name__ == "get_current_tick":
        for args in api_args:
            yield api_func(args)
    else:
        executor = ThreadPoolExecutor(MAX_THREADS)
        for result in executor.map(lambda p: api_func(*p), api_args):
            yield result

def to_dataframe(stock_data, stocks):
    df = pd.DataFrame()
    for i, result in enumerate(stock_data):
        result["stock"] = stocks[i]
        if isinstance(result.index, pd.DatetimeIndex):
            result["date"] = result.index
        df = df.append(result)
    return df


#convert to dict of tuples and remove NaN
# categories = {category[0]: tuple(stock for stock in category[1:] if not pd.isna(stock)) \
#                 for category in list(categories.T.itertuples(index=True)) }