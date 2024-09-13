import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


'''

static webtable

'''

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications") #notificatiob popups disable

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service,options=ops)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

tablerow = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.XPATH,"//table[@name='BookTable']//tr"))
)
tablecol = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.XPATH,"//table[@name='BookTable']//tr/th"))
)

row = len(tablerow)
col = len(tablecol)

for i in range(2,row+1):
    auth = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{str(i)}]/td[2]").text
    if auth == "Mukesh":
        print(driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{str(i)}]/td[1]").text,auth)
time.sleep(10)
driver.quit()