import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
time.sleep(30)

drpcountry_ele = driver.find_elements(By.XPATH,"//select[@id='input-country']")
drpcountry = Select(drpcountry_ele)

drpcountry.select_by_visible_text('India')
drpcountry.select_by_value("10")
drpcountry.select_by_index(13)

alloptions = drpcountry.options #gives the options it has

for opt in alloptions:
    print(opt.text)

driver.quit()