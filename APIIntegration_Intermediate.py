import requests
import json

def get_stock_data():
    url = url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url)

    if(response.statuscode == 200):
        data = response.json()
        last_refreshed = data["Meta Data"] ["3. Last Refreshed"]
        price = data["Time series (5min)"][[laat_refreshed]["1. open"]
        return price
    else:
        return None

    stock_prices = {}
    symbol = "IBM"
    if price is not None:
        stock_prices[symbol] = price

    print(f"{symbol} : {price"} 
                          
