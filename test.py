import requests

def CompanyDetails(Ticker):
    # Define the API endpoint and parameters
    apikey = "29de022d931f42e73af5b5884f4e970d"
    url = f"https://financialmodelingprep.com/api/v3/profile/{Ticker}?apikey={apikey}"
    # Send a GET request to the API and parse the JSON response
    response = requests.get(url)
    company_data = response.json()
    if len(company_data) > 0:
        return company_data[0]
    else:
        return print("there is no values")
    

tickers = ["TSLA", "APPL", "FB", "GOOG" , "MSFT" ,"SBUX","MBG.DE","2222.SR", "CIB" , "QNBK" ,"ETEL" ,"EGS3G0Z1C014.CA" ,"EGS3C251C013.CA"]
data_flow = {}   
for ticker in tickers:
    data = CompanyDetails(ticker)
    data_flow.update({ticker: {"image": data["image"], "price": data["price"], "changes": data["changes"] ,"company Name": data["companyName"]}})

print(data_flow)  
