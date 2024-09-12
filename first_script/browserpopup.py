import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications") #notificatiob popups disable

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service,options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

time.sleep(10)
driver.quit()