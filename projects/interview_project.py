import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(10)
u = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[1]").text

username= u[11:]
print(username)
user = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']"))
)
user.send_keys(username)


p = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[2]").text
password = p[11:]
print(password)


pasw = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Password']"))
)
pasw.send_keys(password)

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()

driver.find_elements()

x = input("enter to quit")
driver.quit()