
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd

matches=[]
matches1=[]
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url="https://odibets.com/"
driver.get(url)
driver.maximize_window()
time.sleep(7)
# html2=requests.get(url).text
with open("odibets.html","r+") as my_file:
    my_file.seek(0)
    my_file.truncate(0)
    my_file.close()

marichu=driver.page_source
# print(marichu)
with open("odibets.html","w",encoding="utf-8") as mar_file:
    mar_file.write(marichu)
    mar_file.close()

html2=marichu.encode('utf-8').strip()
soup=BeautifulSoup(html2,"html.parser")
print(type(soup.prettify()))
print(type(marichu))
print()
def main():
    counter=0
    match_Dict={}
    oddsArr=[]
    hes=0
    mes=1
    try:

        first=WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.XPATH,"(//div[@class='l-events-games-matches'])[2]"))
        )
        print("the element was found")     
        marichu1=soup.find("div",{"class":"l-events-games-matches"}) 
        marichu2=marichu1.findAll("div",class_="t-i")
        for marichus in marichu2:
            print(marichus.string)
            matches.append(marichus.string)
        print(len(matches))
        print(counter)
        while counter < int(len(matches)-1):
                f=matches[counter]
                j=matches[counter+1]
                k=f+" vs "+j
                matches1.append(k)
                counter=counter+2
        odds=marichu1.findAll("span",class_="b")
        for odd in odds:
            # print(odd.string)
            oddsArr.append(odd.string)

        indi_Dict={matches1[mes]:{"1":oddsArr[hes],
                                  "X":oddsArr[hes+1],
                                  "2":oddsArr[hes+2],
                                  "1or2":oddsArr[hes+3],
                                  "Xor2":oddsArr[hes+4],
                                  "1or2":oddsArr[hes+5]}}
        hes=hes+6
        print(indi_Dict)
        df=pd.DataFrame.from_dict(indi_Dict)
        print(df)
        print(f"The matches array{ matches}")
        print()
        print(f"The Matches1 array {matches1}")
        print()
        print(f"The odds array {oddsArr}")
        # fill the dictionary
        for mes in range(len(matches1)-1):
                indi_Dict[matches1[mes]]={"1":oddsArr[hes],
                                  "X":oddsArr[hes+1],
                                  "2":oddsArr[hes+2],
                                  "1or2":oddsArr[hes+3],
                                  "Xor2":oddsArr[hes+4],
                                  "1or2":oddsArr[hes+5]}
                hes=hes+6
                mes=mes+1
        print(indi_Dict)
        
      

    except:
        print("The elements werent located")
main()


