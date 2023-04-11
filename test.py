import requests
url = "https://financialmodelingprep.com/api/v3/stock_news?tickers=AAPL,FB,GOOG,AMZN&page=0&apikey=29de022d931f42e73af5b5884f4e970d"
params = {
        "tickers": "AAPL,FB,GOOG,AMZN",
        "page": "0",
        "apikey": "29de022d931f42e73af5b5884f4e970d"
    }

    # Send a GET request to the API and parse the JSON response
response = requests.get(url, params=params)
data = response.json()
print(data)
