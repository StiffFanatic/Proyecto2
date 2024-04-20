import requests

def get_stock_data(api_key, symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        time_series = data.get("Time Series (Daily)")
        return time_series
    else:
        return None
