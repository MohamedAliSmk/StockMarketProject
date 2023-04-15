import requests
import yfinance as yf
import yfm
import yfinance as yf
import pandas as pd
import requests

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
fetcher = yfm.fetcher()
fetcher.getTicker("goog")
fetcher.fetchInterval()   # read from the db
fetcher.update()           # same as 'yfm update'
#hist = data.history(period="1mo")
#print(hist)
#meta=data.history_metadata
#print(meta)
fetcher = yfm.fetcher()
fetcher.getTicker("goog")
fetcher.fetchInterval()   # read from the db
fetcher.update()           # same as 'yfm update'
#hist = data.history(period="1mo")
#print(hist)
#meta=data.history_metadata
#print(meta)
{'address1': '1 Tesla Road',
 'city': 'Austin',
   'state': 'TX',
     'zip': '78725',
       'country': 'United States',
         'phone': '512 516 8177',
           'website': 'https://www.tesla.com',
             'industry': 'Auto Manufacturers', 'sector': 'Consumer Cyclical', 'longBusinessSummary': 'Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, and internationally. It operates in two segments, Automotive, and Energy Generation and Storage. The Automotive segment offers electric vehicles, as well as sells automotive regulatory credits; and non-warranty after-sales vehicle, used vehicles, retail merchandise, and vehicle insurance services. This segment also provides sedans and sport utility vehicles through direct and used vehicle sales, a network of Tesla Superchargers, and in-app upgrades; purchase financing and leasing services; services for electric vehicles through its company-owned service locations and Tesla mobile service technicians; and vehicle limited warranties and extended service plans. The Energy Generation and Storage segment engages in the design, manufacture, installation, sale, and leasing of solar energy generation and energy storage products, and related services to residential, commercial, and industrial customers and utilities through its website, stores, and galleries, as well as through a network of channel partners; and provision of service and repairs to its energy product customers, including under warranty, as well as various financing options to its solar customers. The company was formerly known as Tesla Motors, Inc. and changed its name to Tesla, Inc. in February 2017. Tesla, Inc. was incorporated in 2003 and is headquartered in Austin, Texas.', 'fullTimeEmployees': 127855, 'companyOfficers': [{'maxAge': 1, 'name': 'Mr. Elon R. Musk', 'age': 50, 'title': 'Technoking of Tesla, CEO & Director', 'yearBorn': 1972, 'fiscalYear': 2022, 'totalPay': 0, 'exercisedValue': 0, 'unexercisedValue': 27819718656}, {'maxAge': 1, 'name': 'Mr. Zachary John Planell Kirkhorn', 'age': 36, 'title': 'Master of Coin & CFO', 'yearBorn': 1986, 'fiscalYear': 2022, 'totalPay': 303000, 'exercisedValue': 1258505, 'unexercisedValue': 205700880}, {'maxAge': 1, 'name': 'Mr. Andrew D. Baglino', 'age': 41, 'title': 'Sr. VP of Powertrain & Energy Engineering', 'yearBorn': 1981, 'fiscalYear': 2022, 'totalPay': 303000, 'exercisedValue': 33866368, 'unexercisedValue': 57355632}, {'maxAge': 1, 'name': 'Mr. Vaibhav  Taneja', 'age': 44, 'title': 'Corp. Controller & Chief Accounting Officer', 'yearBorn': 1978, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Martin  Viecha', 'title': 'Sr. Director for Investor Relations', 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Alan  Prescott', 'age': 43, 'title': 'VP of Legal', 'yearBorn': 1979, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Dave  Arnold', 'title': 'Sr. Director of Global Communications', 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Brian  Scelfo', 'title': 'Sr. Director of Corp. Devel.', 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Jeffrey B. Straubel', 'age': 46, 'title': 'Sr. Advisor', 'yearBorn': 1976, 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Franz  von Holzhausen', 'title': 'Chief Designer', 'exercisedValue': 0, 'unexercisedValue': 0}], 'auditRisk': 9, 'boardRisk': 10, 'compensationRisk': 8, 'shareHolderRightsRisk': 9, 'overallRisk': 9, 'governanceEpochDate': 1680307200, 'compensationAsOfEpochDate': 1672444800, 'maxAge': 86400, 'priceHint': 2, 'previousClose': 185.9, 'open': 183.95, 'dayLow': 182.01, 'dayHigh': 186.28, 'regularMarketPreviousClose': 185.9, 'regularMarketOpen': 183.95, 'regularMarketDayLow': 182.01, 'regularMarketDayHigh': 186.28, 'payoutRatio': 0.0, 'beta': 2.070501, 'trailingPE': 49.46524, 'forwardPE': 33.944954, 'volume': 95331795, 'regularMarketVolume': 95331795, 'averageVolume': 167635690, 'averageVolume10days': 135460930, 'averageDailyVolume10Day': 135460930, 'bid': 184.94, 'ask': 184.98, 'bidSize': 1000, 'askSize': 1400, 'marketCap': 586322345984, 'fiftyTwoWeekLow': 101.81, 'fiftyTwoWeekHigh': 364.07333, 'priceToSalesTrailing12Months': 7.197495, 'fiftyDayAverage': 192.5484, 'twoHundredDayAverage': 213.99438, 'trailingAnnualDividendRate': 0.0, 'trailingAnnualDividendYield': 0.0, 'currency': 'USD', 'enterpriseValue': 572963684352, 'profitMargins': 0.15413, 'floatShares': 2704010527, 'sharesOutstanding': 3169309952, 'sharesShort': 85568280, 'sharesShortPriorMonth': 81397678, 'sharesShortPreviousMonthDate': 1677542400, 'dateShortInterest': 1680220800, 'sharesPercentSharesOut': 0.027, 'heldPercentInsiders': 0.1306, 'heldPercentInstitutions': 0.44852, 'shortRatio': 0.59, 'shortPercentOfFloat': 0.0311, 'impliedSharesOutstanding': 0, 'bookValue': 14.129, 'priceToBook': 13.093637, 'lastFiscalYearEnd': 1672444800, 'nextFiscalYearEnd': 1703980800, 'mostRecentQuarter': 1672444800, 'earningsQuarterlyGrowth': 0.589, 'netIncomeToCommon': 12583000064, 'trailingEps': 3.74, 'forwardEps': 5.45, 'pegRatio': 4.04, 'lastSplitFactor': '3:1', 'lastSplitDate': 1661385600, 'enterpriseToRevenue': 7.034, 'enterpriseToEbitda': 32.855, '52WeekChange': -0.4446823, 'SandP52WeekChange': -0.055894196, 'exchange': 'NMS', 'quoteType': 'EQUITY', 'symbol': 'TSLA', 'underlyingSymbol': 'TSLA', 'shortName': 'Tesla, Inc.', 'longName': 'Tesla, Inc.', 'firstTradeDateEpochUtc': 1277818200, 'timeZoneFullName': 'America/New_York', 'timeZoneShortName': 'EDT', 'uuid': 'ec367bc4-f92c-397c-ac81-bf7b43cffaf7', 'messageBoardId': 'finmb_27444752', 'gmtOffSetMilliseconds': -14400000, 'currentPrice': 185.0, 'targetHighPrice': 300.0, 'targetLowPrice': 24.33, 'targetMeanPrice': 198.73, 'targetMedianPrice': 210.0, 'recommendationMean': 2.4, 'recommendationKey': 'buy', 'numberOfAnalystOpinions': 35, 'totalCash': 22185000960, 'totalCashPerShare': 7.011, 'ebitda': 17439000576, 'totalDebt': 5747999744, 'quickRatio': 0.947, 'currentRatio': 1.532, 'totalRevenue': 81462001664, 'debtToEquity': 12.523, 'revenuePerShare': 26.026, 'returnOnAssets': 0.11847, 'returnOnEquity': 0.32490003, 'grossProfits': 20853000000, 'freeCashflow': 4208124928, 'operatingCashflow': 14723999744, 'earningsGrowth': 0.569, 'revenueGrowth': 0.372, 'grossMargins': 0.25597998, 'ebitdaMargins': 0.21406999, 'operatingMargins': 0.16808, 'financialCurrency': 'USD', 'trailingPegRatio': 1.6688}

NASDAQ_API="zYsazxgkrAQ3aE5ySsgg"
             
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

def getUSPrices(US_tickers):
    # define a list of tickers for the companies you want to get information for
    US_tickers = ["TSLA", "META", "GOOG" , "MSFT" ,"SBUX","MBG.DE","2222.SR"]

    # use yfinance to download the data
    company_data = yf.download(US_tickers, period='1mo', interval='1d')

    # create a DataFrame with the information you want
    US_price = pd.DataFrame({
        'Company': company_data['Close'].columns,
        'Latest Price': company_data['Close'].iloc[-1].values,
        'Price Change': company_data['Close'].iloc[-1].values - company_data['Open'].iloc[-1].values,
    })

