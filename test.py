import requests
import yfm
import yfinance as yf
import pandas as pd
import requests
    
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
    
[{'uuid': '013f3a26-06d7-3bb6-8811-ddbc901f9eec', 'title': 'These Are The Best Robinhood Stocks To Buy Or Watch Now', 'publisher': "Investor's Business Daily", 'link': 'https://finance.yahoo.com/m/013f3a26-06d7-3bb6-8811-ddbc901f9eec/these-are-the-best-robinhood.html', 'providerPublishTime': 1681689554, 'type': 'STORY', 'thumbnail': {'resolutions': [{'url': 'https://s.yimg.com/uu/api/res/1.2/EjStG4yglHr1k.5Itev99w--~B/aD01MzM7dz05NDU7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/ibd.com/559e977a0eb020a047bf3a3c78adf328', 'width': 945, 'height': 533, 'tag': 'original'}, {'url': 'https://s.yimg.com/uu/api/res/1.2/bt8CEXEtSm8_1YwYOU2_kQ--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/ibd.com/559e977a0eb020a047bf3a3c78adf328', 'width': 140, 'height': 140, 'tag': '140x140'}]}, 'relatedTickers': ['UBER', 'NKE', 'GOOGL', '^GSPC']}, {'uuid': 'da914d4d-bc68-3fec-a721-22afddbd4f64', 'title': 'Google scrambles for new search engine as AI creeps in: report', 'publisher': 'Fox Business', 'link': 'https://finance.yahoo.com/news/google-scrambles-search-engine-ai-183451624.html', 'providerPublishTime': 1681670091, 'type': 'STORY', 'thumbnail': {'resolutions': [{'url': 'https://s.yimg.com/uu/api/res/1.2/ZBVut3brt5F6Ou4KM0.HAw--~B/aD03MjA7dz0xMjgwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/fox_business_text_367/38bca49557862314b80559fd17a8b3fa', 'width': 1280, 'height': 720, 'tag': 'original'}, {'url': 'https://s.yimg.com/uu/api/res/1.2/I0nveAlk9bAeQ4H6ScccCQ--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/fox_business_text_367/38bca49557862314b80559fd17a8b3fa', 'width': 140, 'height': 140, 'tag': '140x140'}]}, 'relatedTickers': ['GOOGL']}, {'uuid': '4b858ce6-cf04-38d4-81e1-8acc6c8bf6c6', 'title': '2 Leading Tech Stocks to Buy in 2023 and Beyond', 'publisher': 'Motley Fool', 'link': 'https://finance.yahoo.com/m/4b858ce6-cf04-38d4-81e1-8acc6c8bf6c6/2-leading-tech-stocks-to-buy.html', 'providerPublishTime': 1681660800, 'type': 'STORY', 'thumbnail': {'resolutions': [{'url': 'https://s.yimg.com/uu/api/res/1.2/eLbkkLHt4KRsuGdLFb1DAQ--~B/aD0yNjY3O3c9NDAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/motleyfool.com/273c3aed3ce143b551ef4414f3037e10', 'width': 4000, 'height': 2667, 'tag': 'original'}, {'url': 'https://s.yimg.com/uu/api/res/1.2/5CHRxQfUfQLpbbg09I4YOw--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/motleyfool.com/273c3aed3ce143b551ef4414f3037e10', 'width': 140, 'height': 140, 'tag': '140x140'}]}, 'relatedTickers': ['AMZN', 'GOOGL']}, {'uuid': 'c45aabf2-03d7-37e4-bf9b-47c98cc07807', 'title': 'Deepfake porn could be a growing problem amid AI race', 'publisher': 'AP Finance', 'link': 'https://finance.yahoo.com/news/deepfake-porn-could-growing-problem-152435351.html', 'providerPublishTime': 1681658675, 'type': 'STORY', 'thumbnail': {'resolutions': [{'url': 'https://s.yimg.com/uu/api/res/1.2/MjETBpY0KcUmHxz7rqPptg--~B/aD0zMzMzO3c9NTAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap_finance_articles_694/6e400c1f459695c9e8b523fe13e22a7a', 'width': 5000, 'height': 3333, 'tag': 'original'}, {'url': 'https://s.yimg.com/uu/api/res/1.2/ZzLmaVW_sLx4A9Xwvnx7kA--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/ap_finance_articles_694/6e400c1f459695c9e8b523fe13e22a7a', 'width': 140, 'height': 140, 'tag': '140x140'}]}, 'relatedTickers': ['GOOGL']}, {'uuid': '02806e01-b158-3da6-897a-5980e41ef725', 'title': 'AI Revolution: 2 AI Stocks Billionaires Are Buying Hand Over Fist', 'publisher': 'Motley Fool', 'link': 'https://finance.yahoo.com/m/02806e01-b158-3da6-897a-5980e41ef725/ai-revolution%3A-2-ai-stocks.html', 'providerPublishTime': 1681657200, 'type': 'STORY', 'thumbnail': {'resolutions': [{'url': 'https://s.yimg.com/uu/api/res/1.2/yPBObwWWzIKBRAn4a0r1OQ--~B/aD0xMjcwO3c9MjM1OTthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/motleyfool.com/2899c6802d24b41b5b2c5a299f510344', 'width': 2359, 'height': 1270, 'tag': 'original'}, {'url': 'https://s.yimg.com/uu/api/res/1.2/mNp44HEVSk76ZvqSIqWwpQ--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/motleyfool.com/2899c6802d24b41b5b2c5a299f510344', 'width': 140, 'height': 140, 'tag': '140x140'}]}, 'relatedTickers': ['GOOGL', 'NVDA']}, {'uuid': '6517567e-3448-38b0-97df-e15bf6966f61', 'title': '10 Best FAANG Stocks To Buy Now', 'publisher': 'Insider Monkey', 'link': 'https://finance.yahoo.com/news/10-best-faang-stocks-buy-123935017.html', 'providerPublishTime': 1681648775, 'type': 'STORY', 'thumbnail': {'resolutions': [{'url': 'https://s.yimg.com/uu/api/res/1.2/w8DrQEWdkHsSGWjzdj.Mfg--~B/aD0yMjU7dz00MDA7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/insidermonkey.com/539c1476c92038449b5d6db89592cd32', 'width': 400, 'height': 225, 'tag': 'original'}, {'url': 'https://s.yimg.com/uu/api/res/1.2/RiCItgQHh7x28tYTnVUg6A--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/insidermonkey.com/539c1476c92038449b5d6db89592cd32', 'width': 140, 'height': 140, 'tag': '140x140'}]}, 'relatedTickers': ['ADBE', 'NFLX', 'AAPL', 'GOOGL', 'NVDA', 'AMD', 'MSFT', 'BABA', 'META']}, {'uuid': '9df1fb81-c744-3b36-a73a-9f931874792b', 'title': 'The AI wars will be a bloodbath for investors', 'publisher': 'The Telegraph', 'link': 'https://finance.yahoo.com/news/ai-wars-bloodbath-investors-120000254.html', 'providerPublishTime': 1681646400, 'type': 'STORY', 'thumbnail': {'resolutions': [{'url': 'https://s.yimg.com/uu/api/res/1.2/HpxPQt4Z4NUnG4DGmWJYyg--~B/aD01MzY7dz04NTg7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/the_telegraph_258/511fc2652be60f272d9e302c28460410', 'width': 858, 'height': 536, 'tag': 'original'}, {'url': 'https://s.yimg.com/uu/api/res/1.2/x0u8pDRZDVcxjUhBSrPAsg--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/the_telegraph_258/511fc2652be60f272d9e302c28460410', 'width': 140, 'height': 140, 'tag': '140x140'}]}, 'relatedTickers': ['GOOGL']}, {'uuid': '69852486-621d-30ef-9be6-f6b96cc7880e', 'title': 'GM Ditches Apple CarPlay on EVs as Fight for Your Car’s Screen Intensifies', 'publisher': 'The Wall Street Journal', 'link': 'https://finance.yahoo.com/m/69852486-621d-30ef-9be6-f6b96cc7880e/gm-ditches-apple-carplay-on.html', 'providerPublishTime': 1681646400, 'type': 'STORY', 'thumbnail': {'resolutions': [{'url': 'https://s.yimg.com/uu/api/res/1.2/cGZsAo6mlspyhesDyeYAkA--~B/aD02NDA7dz0xMjgwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/wsj.com/ff01901e31fa154b1c580211ba12de3b', 'width': 1280, 'height': 640, 'tag': 'original'}, {'url': 'https://s.yimg.com/uu/api/res/1.2/bh0tmrpfbyzDhlHtsTkNzQ--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/wsj.com/ff01901e31fa154b1c580211ba12de3b', 'width': 140, 'height': 140, 'tag': '140x140'}]}, 'relatedTickers': ['GOOG', 'GOOGL', 'GM', 'TSLA', 'AAPL']}]         
"""
def getPrice_Change(symbol):
    data=yf.Ticker(symbol)
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

"""def get_stock_data(request, Ticker):
    stock_data = yf.download(Ticker, start='2020-01-01', end='2023-01-01')
    stock_data.reset_index(inplace=True)
    stock_data['Date'] = stock_data['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    response_data = stock_data.to_dict(orient='records')
    return JsonResponse(response_data, safe=False)

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
    return render(request, 'Companys.html', {'data': data})

def stock_prices(request):
    return render(request, 'Companys.html')

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

"""
def getPrice_Change(symbol):
    data=yf.Ticker(symbol)
    Price=data.info['currentPrice']
    Previous_Day=data.info['previousClose']
    change = ((Price - Previous_Day)/ Previous_Day)*100 
    change= round(change,2) 
    if change>0:
        change=f'+ {change}%'
        
    elif change<0:
        change=f'{change}%'
    else:
        change=f'{change}%'
    PAC=[Price,change]
    return PAC


def get_comapny_data(symbol):
    overview_response = yf.Ticker(symbol)
    Company_data = overview_response.info
    company_name=Company_data['shortName']
    company_exchange=Company_data['exchange']
    currency=Company_data['financialCurrency']
    industry=Company_data['industry']
    website=Company_data['website']
    description=Company_data['longBusinessSummary']
    data=[symbol,company_name,company_exchange,currency,industry,description,website]
    return data
    

def get_companydata(symbol):
    # Get the company data
    company = yf.Ticker(symbol)
    data = company.info

    # Get the image
    image_url = data["logo_url"]

    # Get the exchange
    exchange = data["exchange"]

    # Get the company name
    company_name = data["shortName"]

    # Get the currency
    currency = data["currency"]

    # Get the website
    website = data["website"]

    # Get the CEO
    ceo = data["ceo"]

    # Get the description
    description = data["longBusinessSummary"]

    # Get the industry
    industry = data["industry"]

    # Get the sector
    sector = data["sector"]

    # Get the real time price
    real_time_price = data["price"]

    # Get the change
    change = data["change"]

    return {
        "image_url": image_url,
        "exchange": exchange,
        "company_name": company_name,
        "currency": currency,
        "website": website,
        "ceo": ceo,
        "description": description,
        "industry": industry,
        "sector": sector,
        "real_time_price": real_time_price,
        "change": change
    }

import requests
import yfinance as yf
import pandas as pd

def yf_Scraper(symbol):
    data = yf.Ticker(symbol)
    info = data.info
    #print(info)
    # Get stock price and change
    current_price = info['currentPrice']
    previous_close = info['regularMarketPreviousClose']
    price_change = round((current_price - previous_close) / previous_close * 100, 2)
    if price_change > 0:
        price_change = f'+{price_change}%'
    else:
        price_change = f'{price_change}%'
        
    # Get company data
    company_name = info['shortName']
    company_exchange = info['exchange']
    currency = info['financialCurrency']
    industry = info['industry']
    website = info['website']
    description = info['longBusinessSummary']
    
    # Return data as dictionary
    data_dict = {
        'symbol': symbol,
        'current_price': current_price,
        'price_change': price_change,
        'company_name': company_name,
        'company_exchange': company_exchange,
        'currency': currency,
        'industry': industry,
        'description': description,
        'website': website,
    }
    
    return data_dict["current_price"]


data=yf_Scraper("GOOG")
print("TSLA")
"""companies_urls = ['EGX-ORHD'] #get from https://www.tradingview.com/symbols/NASDAQ-AAPL/ Support multiple tickers.
    companies_data = START.get_data(companies_urls) #Get from DataBase or Website
    company = companies_data[0] #get the first company

    company_income_statement = IncomeStatementVisualizer(company_data=company)
    company_balance_sheet = BalanceSheetVisualizer(company_data=company)
    company_cashflow_statement = CashflowStatementVisualizer(company_data=company)
    company_statistics_ratios = StatisticsRatiosVisualizer(company_data=company)
    company_dividents = DividentsVisualizer(company_data=company)
        
    # get company data from Database
    DataBase.Start()
    tables = DataBase.ListTableRows('EGX-ORHD/Company-Data')
    DataBase.Stop()
    s = tables[0][0]  # assuming the first element of the first row is the Ticker
    Tickerexchange = s.split("-")
    Ticker=Tickerexchange[0]
    exchange=Tickerexchange[1]
    price = tables[7][0]
    changes = tables[8][0]
    currency = tables[9][0]    

    # Define a dictionary to hold the financial data
    financial_data = {}

    # Display dividents
    #dividents = company_dividents.dividents()
    #financial_data['dividents'] = dividents

    # Display income statement
    revenue = company_income_statement.revenue()
    operating_income = company_income_statement.operating_income()
    pretax_income = company_income_statement.pretax_income()
    discontinued_operations = company_income_statement.discontinued_operations()
    net_income = company_income_statement.net_income()
    diluted_net_income = company_income_statement.diluted_net_income()
    eps = company_income_statement.eps()
    shares = company_income_statement.shares()
    ebit = company_income_statement.ebit()
    operating_expenses = company_income_statement.operating_expenses()

    financial_data['revenue'] = revenue
    financial_data['operating_income'] = operating_income
    financial_data['pretax_income'] = pretax_income
    financial_data['discontinued_operations'] = discontinued_operations
    financial_data['net_income'] = net_income
    financial_data['diluted_net_income'] = diluted_net_income
    financial_data['eps'] = eps
    financial_data['shares'] = shares
    financial_data['ebit'] = ebit
    financial_data['operating_expenses'] = operating_expenses

    # Display balance sheet
    total_assets_liabilities_equity = company_balance_sheet.total_assets_liabilities_equity()
    current_non_current_assets = company_balance_sheet.current_non_current_assets()
    current_non_current_liabilities = company_balance_sheet.current_non_current_liabilities()
    total_debt_net_debt = company_balance_sheet.total_debt_net_debt()
    book_value_per_share = company_balance_sheet.book_value_per_share()

    financial_data['total_assets_liabilities_equity'] = total_assets_liabilities_equity
    financial_data['current_non_current_assets'] = current_non_current_assets
    financial_data['current_non_current_liabilities'] = current_non_current_liabilities
    financial_data['total_debt_net_debt'] = total_debt_net_debt
    financial_data['book_value_per_share'] = book_value_per_share

    # Display cashflow
    cashflow_operating_investing_financial = company_cashflow_statement.cashflow_operating_investing_financial()
    cashflow_operating_activities = company_cashflow_statement.cashflow_operating_activities()
    cashflow_investing_activities = company_cashflow_statement.cashflow_investing_activities()
    cash_from_financing_activities = company_cashflow_statement.cash_from_financing_activities()

    financial_data['cashflow_operating_investing_financial'] = cashflow_operating_investing_financial
    financial_data['cashflow_operating_activities'] = cashflow_operating_activities
    financial_data['cashflow_investing_activities'] = cashflow_investing_activities
    financial_data['cash_from_financing_activities'] = cash_from_financing_activities

    # Display statistics
    shares_outstanding = company_statistics_ratios.shares_outstanding()
    enterprice_values = company_statistics_ratios.enterprice_values()
    numer_of_employees_shareholders = company_statistics_ratios.numer_of_employees_shareholders()
    price_ratios = company_statistics_ratios.price_ratios()
    return_ratios = company_statistics_ratios.return_ratios()
    margins = company_statistics_ratios.margins()
    dept_ratios = company_statistics_ratios.dept_ratios()
    liquidity_ratios = company_statistics_ratios.liquidity_ratios()

    financial_data['shares_outstanding'] = shares_outstanding
    financial_data['enterprice_values'] = enterprice_values
    financial_data['numer_of_employees_shareholders'] = numer_of_employees_shareholders
    financial_data['price_ratios'] = price_ratios
    financial_data['return_ratios'] = return_ratios
    financial_data['margins'] = margins
    financial_data['dept_ratios'] = dept_ratios
    financial_data['liquidity_ratios'] = liquidity_ratios

    # Add the financial data to the context
    context = {'exchange': exchange,
            'currency': currency,
            'Current_price': price,
            'changes': changes,
            'symbol': Ticker,
            'financial_data': financial_data}
    return render(request, 'Companys.html', context)
"""




"""from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["Fintechers"]
collection = db["Model_stocks"]

tickers = ["TSLA", "APPL", "FB", "GOOG" , "MSFT" ,"SBUX","MBG.DE","2222.SR", "CIB" , "QNBK" ,"ETEL" ,"EGS3G0Z1C014.CA" ,"EGS3C251C013.CA"]
data_flow = []

for ticker in tickers:
    try:
        data = yf_Scraper(ticker)
        data_flow.append(data)
    except KeyError:
        print(f"Error retrieving data for ticker: {ticker}")

# Insert data into MongoDB
collection.insert_many(data_flow)

# Close the MongoDB connection
client.close()
"""