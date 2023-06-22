import json
import yfinance as yf

def save_tickers(companies):
    tickers = {}
    
    for company in companies:
        # Scrape ticker from Yahoo Finance
        try:
            data = yf.Ticker(company)
            info = data.info
            ticker_yf = info['symbol']
            exchange=info['exchange']
            company_name=info['shortName']
    
        except:
            ticker_yf = None
            print("sorry!! yahoo finance ticker isn't correct")
        
        # ticker of TradingView
        company_url=f"{exchange}-{company}"
        ticker_TradingView = company_url
        
        # ticker of investing.com 
        #print to user to enter ticker of the company
        ticker_investing=input(f"please enter ticker of {company_name}:")
        # Add ticker information to dictionary
        tickers[company_name] = {
            'ticker_yf': ticker_yf,
            'ticker_TradingView':ticker_TradingView,
            'ticker_investing': ticker_investing,
        }
    
    # Save tickers to a JSON file
    with open("tickers.json", "w") as f:
        json.dump(tickers, f)


companies = ["AAPL", "GOOGL", "TSLA", "FB"]
save_tickers(companies)