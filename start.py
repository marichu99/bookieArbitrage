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
        more_bets=driver.find_element(By.CSS_SELECTOR,"body.modal-open:nth-child(2) div.ad2hs-prompt:nth-child(15) div.container-fluid:nth-child(8) div.row div.body-content.col-xs-12.col-md-12:nth-child(3) div.row:nth-child(2) div.col-lg-12 div.tab-content div.hidden.active:nth-child(1) div.row.eventRow:nth-child(3) div.col-xs-3.col-sm-2.col-md-2.col-lg-1.more-button.betbooster-more-Button div.col-xs-6.eventAction.betbooster-more-Button-eventAction:nth-child(3) div.mb-wrapper > a.btn.btn-bettingmatch-more.display--flex.flex-align--center.flex-justify--center.line-height--default") 
                                                                            
        more_bets.click()                          
                                                    
        print("More bets achieved")
    except:
        print("something went wrong")  
        time.sleep(60)

 
        
def main():
    usingSelenium()
    # driver.quit()

main()

