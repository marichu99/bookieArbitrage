from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time

# set up the driver
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url to the site
url="https://www.betika.com/en-ke/login"

driver.get(url)

print("were in ")
try:
    number=driver.find_element(By.XPATH,"//input[@placeholder='e.g. 0712 234567']")
    number.send_keys("0799692741")
    password=driver.find_element(By.XPATH,"//input[@type='password']")
    password.send_keys("Password31")
    login=driver.find_element(By.XPATH,"//button[@class='button account__payments__submit session__form__button login button button__secondary']")
    login.click()
    time.sleep(60)
    m=open("marichu.html","w")
    m.write(driver.page_source)
    m.close()
    first=driver.find_element(By.CLASS_NAME,"prebet-match__odd-market__container")                   
    # first.click()
except:
    print("A login error occured")
    time.sleep(5)
    driver.quit()
time.sleep(100)








