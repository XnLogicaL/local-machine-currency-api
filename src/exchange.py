# Author: XnLogicaL
# Licensed under the MIT License

from selenium import webdriver
from selenium.webdriver.common.by import By

class api:
    def get_url(base, to):
        return "https://www.google.com/finance/quote/%s-%s" % (base, to) # Format url with the provided base and to

    def get_data(url: str):
        print("getting latest exchange rates")
        
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless") # Makes the browser invisible.
        browser = webdriver.Firefox(options=options) # Using chrome might be faster, don't forget to change browser options.
        browser.get(url=url)
        
        try:
            return float(browser.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[4]/div/main/div[2]/div[1]/div[1]/c-wiz/div/div[1]/div/div[1]/div/div[1]/div/span/div/div").text) # While XPATH is more reliable, I believe it's a lot slower than class or id.
        finally:
            browser.quit()

def get_latest(base: str, to: str):
    return api.get_data(api.get_url(base, to))
