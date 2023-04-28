from timeit import default_timer as timer
start = timer()
import logging
import sys
import time
import pandas as pd
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pymongo import MongoClient

#logger setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

class START():
    """ Get company data first from DataBase and if not available Scrape it from website """
    companies = []

    @classmethod
    def get_data(cls, companies_urls):
        DataBase.Start() #Connect to DataBase 
        urls_not_in_database = [] #collect urls not found in database
        cls.companies = [] #reset companies variable 

        #run get-company-data process on separate threads
        for url in companies_urls:
            #get the data from DataBase
            company_data = DataBase()
            company_data.GetFromDataBase(company_url=url)

            #if data is not loaded from Database
            if company_data.income_statement is None or \
                company_data.balance_sheet is None or \
                company_data.cashflow_statement is None or \
                company_data.statistics is None or \
                company_data.company_data is None:
                
                #collect companies that needs to be scraped for the website
                urls_not_in_database.append(url)
            
            #if data loaded from DataBase
            else:
                cls.companies.append(company_data)
        
        #get the data from the website
        if urls_not_in_database: #if not empty

            # #start website scraping in separate threads
            max_thread = 4
            with concurrent.futures.ThreadPoolExecutor(max_thread) as executor:
                results = [executor.submit(cls.run_in_separate_thread, url) for url in urls_not_in_database ]
                
                #when webscraping is completed
                for item in concurrent.futures.as_completed(results):
                    company_data = item.result()
                    print(">"*50, type(company_data))
                    cls.companies.append(company_data)
                    DataBase.AddToDatabase(data=company_data)
            
            #start website scraping in single thread:
                for url in urls_not_in_database:
                    company_data = ScrapeTrendingView(company_url=url)
                    cls.companies.append(company_data)
                    DataBase.AddToDatabase(data=company_data)

        
        DataBase.Stop() #Disconnect Database 
        return cls.companies #return company-data

    @classmethod
    def run_in_separate_thread(cls, url):
        company_data = ScrapeTrendingView(company_url=url)
        return(company_data)

class DataBase:
    def __init__(self, host='localhost', port=27017, db_name='Fintechers'):
        self.host = host
        self.port = port
        self.db_name = db_name

        
    def Start(self):
        self.client = MongoClient(self.host, self.port)
        
    def Stop(self):
        self.client.close()
        
    def ReadFromDatabase(self, collection_name):
        collection = self.client[self.db_name][collection_name]
        data = []
        for doc in collection.find():
            data.append(doc)
        if len(data) == 0:
            return []
        else:
            return data[0]

    @classmethod
    def AddToDatabase(cls, data):
        """
        data = Instance of ScrapeTrendingView() Class
        """

        cls.StoreInDatabase(data=data.income_statement, collection_name=data.company_url + '/Income-Statement')
        cls.StoreInDatabase(data=data.balance_sheet, collection_name=data.company_url + '/balance-Sheet')
        cls.StoreInDatabase(data=data.cashflow_statement, collection_name=data.company_url + '/Cashflow-Statement')
        cls.StoreInDatabase(data=data.statistics, collection_name=data.company_url + '/Ratios')
        if data.dividents is not None:
            cls.StoreInDatabase(data=data.dividents, collection_name=data.company_url + '/Dividents')
        cls.StoreInDatabase(data=data.company_data, collection_name=data.company_url + '/Company-Data')       

    @classmethod
    def StoreInDatabase(self, data, collection_name):
        """
        Stores data in a MongoDB collection.
        
        Parameters:
        - data (pandas.DataFrame): The data to be stored.
        - collection_name (str): The name of the collection to store the data in.
        """
        with MongoClient(self.host, self.port, self.database) as db:
            collection = db[collection_name]
            collection.insert_many(data.to_dict('records'))


    def GetFromDataBase(self, company_url):
        # get financial data from database
        self.income_statement = self.ReadFromDatabase(collection_name=company_url + "/Income-Statement")
        self.balance_sheet = self.ReadFromDatabase(collection_name=company_url + "/balance-Sheet")
        self.cashflow_statement = self.ReadFromDatabase(collection_name=company_url + "/Cashflow-Statement")
        self.statistics = self.ReadFromDatabase(collection_name=company_url + "/Ratios")
        self.company_data = self.ReadFromDatabase(collection_name=company_url + "/Company-Data")

        if self.company_data is not None:
            self.company_name = self.company_data.get('company_name')
            self.company_ticker = self.company_data.get('company_ticker')
            self.company_url = self.company_data.get('company_url')
            dividents_exists = self.company_data.get('dividents')

            if dividents_exists == '1':
                self.dividents = self.ReadFromDatabase(collection_name=company_url + "/Dividents")
            else:
                self.dividents = None
        
class ScrapeTrendingView(): 

    maximum_number_of_colapsed_rows = 50
    def __init__(self, company_url,*args, **kwargs):
        """
        company_url = Exchange-Ticker \n
        company_url = NASDAQ-AAPL \n
        """
        super(ScrapeTrendingView, self).__init__(*args, **kwargs)
        # innitialize and set chrome-webdriver options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        #chrome_options.add_argument("--window-size=1000,1080")
        #chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
        self.driver.implicitly_wait(2)
        self.time_sleep = 2
        #self.driver.maximize_window()
        self.scrapeIncomeStatement(company_url=company_url) #start Income-Statement scraping
        self.scrapeBalanceSheet(company_url=company_url) #start balance-Sheet scraping
        self.scrapeCashFlow(company_url=company_url) #start Cashflow-Statement scraping
        self.scrapeStatistics(company_url=company_url) #start Ratios scraping
        self.scrapeDividents(company_url=company_url) #start Dividents scraping
        self.scrapeCompanyData(company_url = company_url) #start Company-Data scraping
        #add additional data to dataframe
        self.companyData_to_dataframe()
        self.driver.close()
    def scrapeIncomeStatement(self, company_url):
        self.income_statement_url = f"https://www.tradingview.com/symbols/{company_url}/financials-income-statement/?selected="

        self.driver.get(self.income_statement_url)
        time.sleep(self.time_sleep)
        self.switch_annual_data()
        # expand income-statement collapsed rows
        i = 0
        while True:
            i = i+1
            if i >self.maximum_number_of_colapsed_rows:
                logging.error(f'Break While loop i={i}')
                break
            try:
                expand_arrow_xpath = "//span[@class='arrow-_PBNXQ7k']"
                expand_arrow_element = self.driver.find_element(by=By.XPATH ,value= expand_arrow_xpath)
                expand_arrow_element.click()
            except:
                break
        # scrape the data
        output= self.scrape_the_data(self.income_statement_url)
        self.income_statement = self.scraped_data_to_dataframe(output=output)
    def scrapeBalanceSheet(self, company_url):
        logger.info('Start balance Sheet Scrape')
        self.balanse_sheet_url = "https://www.tradingview.com/symbols/" + \
            company_url + "/financials-balance-sheet/?selected="
        self.driver.get(self.balanse_sheet_url)
        time.sleep(self.time_sleep)

        self.switch_annual_data()
        # expand balance-sheet collapsed-rows level-2
        i = 0
        while True:
            logger.info('Start Expanding balance Sheet Rows Level-2')
            i = i+1
            if i >  self.maximum_number_of_colapsed_rows:
                logging.error(f'Break While loop i={i}')
                break
            try:
                expand_arrow_xpath = "//span[@class='arrow-_PBNXQ7k hasChanges1-_PBNXQ7k']"
                expand_arrow_element = self.driver.find_element(by=By.XPATH,value=expand_arrow_xpath)
                expand_arrow_element.click()
                # print(expand_arrow_element.if_exists)
            except:
                logger.info('End Expanding balance Sheet Rows Level-2')
                break
        # scrape the data
        output = self.scrape_the_data(self.balanse_sheet_url)
        self.balance_sheet = self.scraped_data_to_dataframe(output=output)
    def scrapeCashFlow(self, company_url):

        logger.info('Start CashFlow Scrape')
        self.cashflow_url = "https://www.tradingview.com/symbols/" + \
            company_url + "/financials-cash-flow/?selected="

        self.driver.get(self.cashflow_url)
        time.sleep(self.time_sleep)

        self.switch_annual_data()
        # expand cash-flow collapsed-rows level-2
        i = 1
        while True:
            logger.info('Start Expanding CashFlow Rows Level-2')
            if i > 20:
                logger.info(f'Break While loop i={i}')
                break
            try:
                expand_arrow_xpath = "//span[@class='arrow-_PBNXQ7k']"
                expand_arrow_element = self.driver.find_element(by=By.XPATH,value=
                    expand_arrow_xpath)
                expand_arrow_element.click()
                # print(expand_arrow_element.if_exists)
                i += 1
            except:
                logger.info('End Expanding CashFlow Rows Level-2')
                break

        # reset i to 1 for the next loop
        i = 1
        # expand cash-flow collapsed-rows level-1
        while True:
            logger.info('Start Expanding CashFlow Rows Level-1')
            if i > 20:
                logger.info(f'Break While loop i={i}')
                break
            try:
                expand_arrow_xpath = "//span[@class='arrow-_PBNXQ7k hasChanges-_PBNXQ7k']"
                expand_arrow_element = self.driver.find_element(by=By.XPATH,value=
                    expand_arrow_xpath)
                expand_arrow_element.click()
                # print(expand_arrow_element.if_exists)
                i += 1
            except:
                logger.info('End Expanding CashFlow Rows Level-1')
                break

        # scrape the data
        output = self.scrape_the_data(self.cashflow_url)
        self.cashflow_statement = self.scraped_data_to_dataframe(output=output)     
    def scrapeStatistics(self, company_url):
        logger.info('Start Statistics Scrape')
        self.statistics_url = "https://www.tradingview.com/symbols/" + company_url + "/financials-statistics-and-ratios/?selected="
        self.driver.get(self.statistics_url)
        time.sleep(self.time_sleep)
        self.switch_annual_data()
        statistics_table_xpath = "//*[@id='js-category-content']/div[2]/div/div/div[4]/div/div[1]/div/div[3]"
        statistics_table_rows = self.driver.find_elements(by=By.XPATH, value=statistics_table_xpath)
        # for item in financial_table[1]:
        #     print(item)

        # print(self.financial_table.text)
        # print(len(statistics_table_rows))
        output = []
        for item in statistics_table_rows:
            item_list = item.text.splitlines()
            output_temp = []
            # skip non-data items like Key stats, Profitability ratios, Liquidity ratios, Solvency ratios
            if len(item_list) == 1:
                continue
            else:
                for i in range(len(item_list)):
                    output_temp.append(item_list[i].replace(
                        '\u202a', '').replace('\u202c', ''))
                # print(temp[i])
                # print(type(temp), len(temp))
                # print(temp)
                output.append(output_temp)
        # for item in output:
        #     print(len(item),item)
        #     pass
        self.statistics = self.scraped_data_to_dataframe(output=output)
    def scrapeDividents(self,company_url):
        logger.info('Start Dividents Scrape')
        self.dividents_url = "https://www.tradingview.com/symbols/" + company_url + "/financials-dividents/?selected="
        self.driver.get(self.dividents_url)
        time.sleep(self.time_sleep)
        # scrape dividents
        try: #if dividents exists
            output = self.scrape_the_data()
            self.dividents = self.scraped_data_to_dataframe(output=output)
        except: #if dividents not exists, return none
             self.dividents = None
        # print(self.dividents)
    def scrapeCompanyData(self, company_url):
        self.company_data_url = "https://www.tradingview.com/symbols/" + company_url + "/technicals/"
        self.driver.get(self.company_data_url)
        time.sleep(self.time_sleep)
        self.company_url = company_url
        company_name_css = "#js-category-content > div.technicals-root > div > div > div.container-PzISMB5Q > div"
        company_name_element = self.driver.find_element(By.CSS_SELECTOR, company_name_css)
        self.company_name = company_name_element.text
        # print(self.company_name)
        price_xpath = "//*[@id='js-category-content']/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]/span"
        price_element = self.driver.find_element(By.XPATH, price_xpath)
        self.price = price_element.text
        changes_xpath = "//*[@id='js-category-content']/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[2]/span[2]"
        changes_element = self.driver.find_element(By.XPATH, changes_xpath)
        self.changes = changes_element.text
        logo_xpath = "//*[@id='js-category-content']/div[1]/div[1]/div/div/div/div[1]/img[2]"
        logo_element = self.driver.find_element(By.XPATH, logo_xpath)
        self.logo = logo_element.text
        curr_xpath = "//*[@id='js-category-content']/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[2]/span[1]"
        curr_element = self.driver.find_element(By.XPATH, curr_xpath)
        self.curr = curr_element.text
    def companyData_to_dataframe(self):
        data = {'company_url':self.company_url,'income_statement_url': self.income_statement_url,'balanse_sheet_url': self.balanse_sheet_url,'cashflow_url': self.cashflow_url,'statistics_url': self.statistics_url,   'company_data_url': self.company_data_url,  'company_name':self.company_name,    'price':self.price,    'changes':self.changes,  'stock currency':self.curr,  'logo_url':self.logo }  
        if self.dividents is None:
            data.update({"dividents": False})
        else:
            data.update({"dividents": True})
        self.company_data = pd.DataFrame.from_dict(data, orient='index', columns=['value'])
    def switch_annual_data(self):
        annual_button_xpath = "//*[@id='FY']"
        annual_button_element = self.driver.find_element(by=By.XPATH, value=annual_button_xpath)
        annual_button_element.click()
    def scraped_data_to_dataframe(self, output):
        output_index = ['Date'] + output[0][1:]
        output_values = []
        output_colums = output[0][1:].replace('(', '').replace(')', '').replace(',', '').split(' ')
        self.currency = output[0][0].replace('Currency: ', '')
        # print(self.currency)
        for i in range(1, len(output)):
            output_index.append(output[i][0])
            output_values.append(output[i][1:])
        # apply neccessery correction to fix the values-data
        output_values = self.fix_data_values(input_data=output_values)
        df = pd.DataFrame(output_values, columns=output_colums, index=output_index, index_col='Date')  # add scraped data to dataframe
        return df
    def scrape_the_data(self):
        financial_table_xpath = "//*[@id='js-category-content']/div[2]/div/div"
        financial_table_rows = self.driver.find_elements(by=By.XPATH, value=financial_table_xpath)
        output = []
        number_of_columns = len(financial_table_rows[0].text.split())
        for item in financial_table_rows:
            item_list = item.text.splitlines()
            output_temp = []
            if len(item_list) == number_of_columns: # rows without YOY-grow

                for i in range(len(item_list)):
                    output_temp.append(item_list[i].replace(
                        '\u202a', '').replace('\u202c', ''))
            else:  # rows with YOY-grow
                if 'YoY Growth' in item_list:  # Quarterly
                    for i in range(1, len(item_list), 2): # skip YOY-grow row
                        output_temp.append(item_list[i].replace(
                            '\u202a', '').replace('\u202c', ''))
                else:  # Anual report
                    output_temp.append(item_list[0])
                    for i in range(1, len(item_list), 2):  # skip YOY-grow row
                        output_temp.append(item_list[i].replace(
                            '\u202a', '').replace('\u202c', ''))
            output.append(output_temp)
        return output
    def fix_data_values(self, input_data):
        output = []
        for row in input_data:
            output_row = []
            for item in row:
                # print(f'item={item}')
                if '−' in item:  # convert minus sign to real minus, for some reason the sign is not recognized as minus
                    item = item.replace('−', '-')
                if 'T' in item:  # convert Trillion-values to numeric
                    item = item.replace('T', '')
                    item = float(item)
                    item = item*1000000000000
                    # item = int(item)
                elif 'B' in item:  # convert Billion-values to numeric
                    item = item.replace('B', '')
                    item = float(item)
                    item = item*1000000000
                    # item = int(item)
                elif 'M' in item:  # convert Milion-values to numeric
                    item = item.replace('M', '')
                    item = float(item)
                    item = item*1000000
                    # item = int(item)
                elif 'K' in item:  # convert Thousants-values to numeric
                    item = item.replace('K', '')
                    item = float(item)
                    item = item*1000
                    # item = int(item)
                if isinstance(item, str):  # if item is not integer (0.00, ---, -)
                    if '—' in item:  # set value to None
                        item = None
                    elif '.' in item:  # convert value to float
                        item = float(item)
                if self.currency != 'USD':  # convert values to USD
                    if self.currency == 'KRW':
                        self.multiplier = 0.000700680009950
                    # check if item is int or float
                    if isinstance(item, float) or isinstance(item, int):
                        item = item*self.multiplier
                output_row.append(item)
            output.append(output_row)
        return output
    

companies_urls = ['NASDAQ-TLSA'] 
scrap = ScrapeTrendingView(companies_urls)
df_of_income=scrap.scrapeIncomeStatement(companies_urls)
print(type(df_of_income))