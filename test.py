import requests
import yfinance as yf
import yfm
def CompanyDetails(Ticker):
    # Define the API endpoint and parameters
    apikey = "8263508c794d9fc6c347f4670860b1a8"
    url = f"https://financialmodelingprep.com/api/v3/profile/{Ticker}?apikey={apikey}"
    # Send a GET request to the API and parse the JSON response
    response = requests.get(url)
    company_data = response.json()
    if len(company_data) > 0:
        return company_data[0]
    else:
        return print("there is no values")
    
""""
tickers = ["TSLA", "APPL", "FB", "GOOG" , "MSFT" ,"SBUX","MBG.DE","2222.SR", "CIB" , "QNBK" ,"ETEL" ,"EGS3G0Z1C014.CA" ,"EGS3C251C013.CA"]
data_flow = {}   
for ticker in tickers:
    data = CompanyDetails(ticker)
    data_flow.update({ticker: {"image": data["image"], "price": data["price"], "changes": data["changes"] ,"company Name": data["companyName"]}})

print(data_flow)  

"""
def getPrice_Change(symbol):
    tickers = yf.Tickers('TSLA APPL FB GOOG MSFT SBUX MBG.DE 2222.SR CIB QNBK ETEL EGS3G0Z1C014.CA EGS3C251C013.CA')
    data=yf.Tickers(symbol)
    Price=data.info['currentPrice']
    Previous_Day=data.info['previousClose']
    change = ((Price - Previous_Day)/ Previous_Day)*100 
    change= round(change,2) 
    if change>0:
        change=f'+ {change}%'
        
    elif change<0:
        change=f'- {change}%'
    else:
        change=f'{change}%'
    return Price,change
tickers = ["TSLA", "APPL", "FB", "GOOG" , "MSFT" ,"SBUX","MBG.DE","2222.SR", "CIB" , "QNBK" ,"ETEL" ,"EGS3G0Z1C014.CA" ,"EGS3C251C013.CA"]
fetcher = yfm.fetcher()
fetcher.getTicker("goog")  # read from the db
fetcher.update()           # same as 'yfm update'
#hist = data.history(period="1mo")
#print(hist)
#meta=data.history_metadata
#print(meta)
