from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def scrape_stock_data(symbol):
    # Set up the Selenium webdriver with the Chrome browser
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    # Define the URL for the stock
    url = f"https://www.investing.com/equities/{symbol}-company-profile"

    # Navigate to the URL
    driver.get(url)
    """
    # Wait for the close button to be visible
    close_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="PromoteSignUpPopUp"]/div[2]/i'))
    )
    ads_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="closeIconHit"]'))
    )
    
    language_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="topAlertBarContainer"]/div/div[3]/a[1]'))
    )
    # Click on the close button
    close_button.click()
    ads_button.click()
    language_button.click()
    """
    # Find the stock logo, price, and change using the Selenium webdriver
    stock_price = driver.find_element(By.XPATH, "//*[@id='last_last']").text
    stock_change = driver.find_element(By.XPATH, "//*[@id='quotes_summary_current_data']/div[1]/div[2]/div[1]/span[4]").text
    company_name = driver.find_element(By.CSS_SELECTOR, "#leftColumn > div.instrumentHead.im-ad-matched > h1").text
    company_exchange = driver.find_element(By.CSS_SELECTOR, "#DropdownBtn > i.btnTextDropDwn.arial_12.bold").text
    currency = driver.find_element(By.CSS_SELECTOR, "#quotes_summary_current_data > div.left.current-data > div.inlineblock > div.bottom.lighterGrayFont.arial_11 > span:nth-child(4)").text
    industry = driver.find_element(By.XPATH, '//*[@id="leftColumn"]/div[8]/div[1]/a').text
    description = driver.find_element(By.XPATH, '//*[@id="profile-fullStory-showhide"]').text
    website = driver.find_element(By.XPATH, '//*[@id="leftColumn"]/div[10]/div[1]/div[4]/span[3]/a').get_attribute("href")
    Volume = driver.find_element(By.XPATH, '//*[@id="quotes_summary_secondary_data"]/div/ul/li[1]/span[2]/span').text 
    empNumber = driver.find_element(By.XPATH, '//*[@id="leftColumn"]/div[8]/div[3]/p').text 
    EquityType = driver.find_element(By.XPATH, '//*[@id="leftColumn"]/div[8]/div[4]/p').text 
    # Quit the Selenium webdriver
    #driver.quit()

    # Return the results as a dictionary
    return {
        "price": stock_price,
        "change": stock_change,
        "company_name": company_name,
        "company_exchange": company_exchange,
        "currency": currency,
        "industry": industry,
        "description": description,
        "website": website,
        "Volume":Volume,
        "Employees":empNumber,
        "Equity Type":EquityType
    }

# Call the function with the stock symbol for Apple Inc.
data = scrape_stock_data("tesla-motors")

# Print the results
print("Stock price:", data["price"])
print("Stock change:", data["change"])
print("Company name:", data["company_name"])
print("Company exchange:", data["company_exchange"])
print("Currency:", data["currency"])
print("Industry:", data["industry"])
print("Description:", data["description"])
print("Website:", data["website"])
