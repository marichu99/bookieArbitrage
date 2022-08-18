from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
# initialise
chrOptions=Options()
chrOptions.add_experimental_option("excludeSwitches",["enable-automation"])
chrOptions.add_experimental_option("useAutomationExtension",False)
chrOptions.add_argument('--disable-blink-features=AutomationControlled')
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrOptions)
county1=["'BARINGO'","'BOMET'","'BUNGOMA'","'BUSIA'","'DIASPORA'","'ELGEYO/MARAKWET'","'EMBU'","'GARISSA'","'HOMA BAY'","'ISIOLO'","'KAJIADO'","'KAKAMEGA'","'KERICHO'","'KIAMBU'","'KILIFI'","'KIRINYAGA'","'KISII'","'KISUMU'","'KITUI'","'KWALE'","'LAIKIPIA'","'LAMU'","'MACHAKOS'","'MAKUENI'"]
county2=["'MURANG'A'","'NAIROBI CITY'","'NAKURU'","'NANDI","'NAROK'","'NYAMIRA'","'NYANDARUA'","'NYERI'","'SAMBURU'","'SIAYA'","'TAITA TAVETA'","'TANA RIVER'","'THARAKA-NITHI'","'TRANS NZOIA'","'TURKANA'","'UASIN GISHU'","'VIHIGA'","'WAJIR'","'WEST POKOT'","'MANDERA'","'MARSABIT'","'MERU'","'MIGORI'","'MOMBASA'"]





def main():
    driver.get("https://forms.iebc.or.ke/#/")

    try:
        main = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"(//div[@class='q-field__control relative-position row no-wrap'])[3]"))
        )
        selectForm34=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"(//div[@id='f_ef9ea4d9-7b46-416b-bf0a-8e5c360c1938_1'])[1]"))
        )
        m=open("test.html","w")
        m.write(driver.page_source)
        m.close()
        main.click()
        selectForm34.click()
        
    except:
        print("element not found")
        time.sleep(10)
        driver.quit()

    
    
main()
