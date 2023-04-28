#import classes
from TrandingViewClasses import *

companies_urls = ['EGX-ORHD'] #get from https://www.tradingview.com/symbols/NASDAQ-AAPL/ Support multiple tickers.
companies_data = START.get_data(companies_urls) #Get from DataBase or Website
company = companies_data[0] #get the first company

company_income_statement = IncomeStatementVisualizer(company_data=company)
company_balance_sheet = BalanceSheetVisualizer(company_data=company)
company_cashflow_statement = CashflowStatementVisualizer(company_data=company)
company_statistics_ratios = StatisticsRatiosVisualizer(company_data=company)
company_dividents = DividentsVisualizer(company_data=company)
