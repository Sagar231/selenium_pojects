import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#opens alert window
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(4)

alterwindow = driver.switch_to.alert
print(alterwindow.text)
alterwindow.send_keys("welcome")

#alterwindow.accept() #close using ok button
alterwindow.dismiss() #close using cancel button
time.sleep(5)
driver.quit()

