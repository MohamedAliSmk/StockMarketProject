import asyncio
import json
import yfinance as yf
from channels.generic.websocket import AsyncWebsocketConsumer

class StockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        self.tickers = ["TSLA", "APPL", "FB", "GOOG" , "MSFT" ,"SBUX","MBG.DE","2222.SR", "CIB" , "QNBK" ,"ETEL" ,"EGS3G0Z1C014.CA" ,"EGS3C251C013.CA"]
        self.interval = 5 # Update interval in seconds

        while True:
            await asyncio.sleep(self.interval)
            stocks = []
            for ticker in self.tickers:
                try:
                    stock = yf.Ticker(ticker)
                    print(stock)
                    price = stock.info['currentPrice']
                    #change = stock.info['regularMarketChangePercent']
                    stocks.append({
                        'symbol': ticker,
                        'price': price,
                     #   'change': change
                    })
                except Exception as e:
                    stocks.append({
                        'symbol': ticker,
                        'error_message': str(e)
                    })

            await self.send(text_data=json.dumps({
                'type': 'stock_data',
                'data': stocks
            }))
