import requests

def get_stock_data(api_key, symbol, url):
    full_url = f"{url}&symbol={symbol}&outputsize=full&apikey={api_key}"
    response = requests.get(full_url)

    if response.status_code == 200:
        data = response.json()
        time_series = data.get("Time Series (Daily)")
        return time_series
    else:
        return None
