import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)


'''
syntext = http://username:password @test.com
'''
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

#opens alert window
time.sleep(5)
driver.quit()