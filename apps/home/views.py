from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,HttpResponse
import yfinance as yf
import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go
import json
import requests
from django.utils.translation import gettext as _
import matplotlib.pyplot as plt
import io
import urllib, base64 

from django.http import JsonResponse

def stocks(request):
    companies = ["TSLA", "APPL", "FB", "GOOG" , "MSFT" ,"SBUX","MBG.DE","2222.SR", "CIB" , "QNBK" ,"ETEL" ,"EGS3G0Z1C014.CA" ,"EGS3C251C013.CA"]
    data = {}
    for company in companies:
        stock = yf.Ticker(company)
        data[company] = {
            'price': stock.info['currentPrice'],
            'change': stock.info['regularMarketChange'],
        }
        print(data)
    return render(request, 'companys.html', {'data': data})

def stock_prices(request):
    return render(request, 'companys.html')

def stocks_data(request):
    companies =  ["TSLA", "APPL", "FB", "GOOG" , "MSFT" ,"SBUX","MBG.DE","2222.SR", "CIB" , "QNBK" ,"ETEL" ,"EGS3G0Z1C014.CA" ,"EGS3C251C013.CA"]
    data = {}
    for company in companies:
        stock = yf.Ticker(company)
        data[company] = {
            'price': stock.info['currentPrice'],
            
            #'change': stock.info['regularMarketChange'],
        }
        
    return JsonResponse(data)


def get_news_data(stock):
    api_key = '29de022d931f42e73af5b5884f4e970d'
    url = f"https://financialmodelingprep.com/api/v3/stock_news?{stock}&page=0&apikey={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data
    

#@login_required(login_url="/login/")
def index(request):   
    language = request.GET.get("lang", "en") # retrieve language preference from GET parameter or default to "en"
    context = {"language": language}
    return render(request, 'index.html', context)

def setting(request):
    return render(request, "setting.html")

def profile(request):
    return render(request, "profile.html")
def Companys(request, Ticker):  
    # Define the API endpoint and parameters
    apikey = "29de022d931f42e73af5b5884f4e970d"
    url = f"https://financialmodelingprep.com/api/v3/profile/{Ticker}?apikey={apikey}"
    # Send a GET request to the API and parse the JSON response
    response = requests.get(url)
    if response.status_code == 200:
        company_data = response.json()
        if len(company_data) > 0:
            company_data = company_data[0]
            # Extract company information
            price = company_data['price']
            mktCap = company_data['mktCap']
            volAvg = company_data['volAvg']
            changes = company_data['changes']
            currency = company_data['currency']
            exchange = company_data['exchange']
            exchangeShortName = company_data['exchangeShortName']
            industry = company_data['industry']
            website = company_data['website']
            description = company_data["description"]
            ceo = company_data['ceo']
            sector = company_data['sector']
            country = company_data['country']
            image = company_data['image']
            return render(request, "Companys.html", context={
                "Ticker": Ticker,
                "price": price,
                "mktCap": mktCap,
                "volAvg": volAvg,
                "changes": changes,
                "currency": currency,
                "exchange": exchange,
                "exchangeShortName": exchangeShortName,
                "industry": industry,
                "website": website,
                "description": description,
                "ceo": ceo,
                "sector": sector,
                "country": country,
                "image": image,
            })
 
def LastNews(request):

    # Define the API endpoint and parameters
    url = "https://financialmodelingprep.com/api/v3/stock_news?tickers={tickers}&{page}=0&apikey={apikey}"
    params = {
        "tickers": "AAPL,FB,GOOG,AMZN",
        "page": "0",
        "apikey": "29de022d931f42e73af5b5884f4e970d"
    }

    # Send a GET request to the API and parse the JSON response
    response = requests.get(url, params=params)
    data = response.json()
    print(data)

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Clean up the DataFrame by dropping unnecessary columns
    df.drop(["image", "site", "text"], axis=1, inplace=True)

    # Convert the date column to a datetime object
    df["date"] = pd.to_datetime(df["date"])
    print( df["date"])

    # Group the news by date and ticker and count the number of news items
    df_grouped = df.groupby(["date", "ticker"]).count().reset_index()

    # Pivot the DataFrame to get the ticker symbols as columns
    df_pivoted = df_grouped.pivot(index="date", columns="ticker", values="title")

    # Fill any missing values with 0
    df_pivoted.fillna(0, inplace=True)

    # Plot the data using Matplotlib and save it to a buffer
    buf = io.BytesIO()
    df_pivoted.plot(kind="line", figsize=(10, 6))
    plt.title("Number of news items by date and ticker")
    plt.xlabel("Date")
    plt.ylabel("Number of news items")
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Encode the buffer to base64 and generate a data URI
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    # Render the template and pass the data URI as a context variable
    return render(request, "Companys.html", context={"plot_path": uri})

def Trending(request):
    return render(request, "Trending.html")

def chart(request):
      # Here we use yf.download function
    data = yf.download(
        
        # passes the ticker
        tickers=['CIB', 'AMZN', 'QCOM', 'META', 'NVDA', 'JPM'],
        
        group_by = 'ticker',
        
        threads=True, # Set thread value to true
        
        # used for access data[ticker]
        period='1mo', 
        interval='1d'
    
    )

    data.reset_index(level=0, inplace=True)

    fig_left = go.Figure()
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['CIB']['Adj Close'], name="CIB")
            )
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['AMZN']['Adj Close'], name="AMZN")
            )
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['QCOM']['Adj Close'], name="QCOM")
            )
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['META']['Adj Close'], name="META")
            )
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['NVDA']['Adj Close'], name="NVDA")
            )
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['JPM']['Adj Close'], name="JPM")
            )
    fig_left.update_layout(paper_bgcolor="#14151b", plot_bgcolor="#14151b", font_color="white")

    plot_div_left = plot(fig_left, auto_open=False, output_type='div')


    # ================================================ To show recent stocks ==============================================
    
    df1 = yf.download(tickers = 'CIB', period='1d', interval='1d')
    df2 = yf.download(tickers = 'AMZN', period='1d', interval='1d')
    df3 = yf.download(tickers = 'GOOGL', period='1d', interval='1d')
    df4 = yf.download(tickers = 'UBER', period='1d', interval='1d')
    df5 = yf.download(tickers = 'TSLA', period='1d', interval='1d')
    df6 = yf.download(tickers = 'TWTR', period='1d', interval='1d')

    df1.insert(0, "Ticker", "CIB")
    df2.insert(0, "Ticker", "AMZN")
    df3.insert(0, "Ticker", "GOOGL")
    df4.insert(0, "Ticker", "UBER")
    df5.insert(0, "Ticker", "TSLA")
    df6.insert(0, "Ticker", "TWTR")

    df = pd.concat([df1, df2, df3, df4, df5, df6], axis=0)
    df.reset_index(level=0, inplace=True)
    df.columns = ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume']
    convert_dict = {'Date': object}
    df = df.astype(convert_dict)
    df.drop('Date', axis=1, inplace=True)

    json_records = df.reset_index().to_json(orient ='records')
    recent_stocks = []
    recent_stocks = json.loads(json_records)

    # ================================================= Load Ticker Table ================================================
    ticker_df = pd.read_csv('apps/Data/new_tickers.csv') 
    json_ticker = ticker_df.reset_index().to_json(orient ='records')
    ticker_list = []
    ticker_list = json.loads(json_ticker)

    return render(request, 'chart.html', {
        'plot_div_left': plot_div_left,
        'recent_stocks': recent_stocks,
        'ticker_list':ticker_list,

    })
  
def Community(request):
    return render(request, "Community.html")
