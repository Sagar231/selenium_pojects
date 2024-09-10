import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks = driver.find_elements(By.TAG_NAME,'a')
count = 0

for link in alllinks:
    url = link.get_attribute('href')
    try:
        res= requests.head(url)
        if res.status_code>=400:
            print(url,"  -> is broken")
            count+=1
        else:
            print(url, "  -> is valid")
    except:
        print("Not working")
print(count)

driver.quit()