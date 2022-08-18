# import webdriver

from selenium import webdriver
# import the web keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from numpy import spacing
import requests
import urllib.request
import re

# specify the path
PATH=r"C:\xampp\htdocs\WebScrapper\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open up youtubecd 
def usingSelenium():
    
    # print(driver.page_source)
    # wait for the element to exist
    try:
        driver.get("https://www.betway.co.ke/")  
        search=driver.find_element(By.XPATH,"//input[@id='MobileNumber']")
        search.send_keys("0799692741")
        search1=driver.find_element(By.XPATH,"//input[@id='Password']")
        search1.send_keys("Password31")
        login=driver.find_element(By.ID,"Login")
        login.click()
        print("Login successful")
        more_bets=WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,"(//a[contains(@class,'')])[180]"))
            )
        more_bets.click()                        
        print("More bets achieved")
        time.sleep(50)
        driver.quit()                                                                            
    except:
        print("something went wrong")  
        time.sleep(60)
        driver.quit()

        
def main():
    usingSelenium()
    # driver.quit()

main()

