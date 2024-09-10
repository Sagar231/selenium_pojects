import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)


'''
switch_to.frame(name of the frame)
switch_to.frame(id of the frame)
switch_to.frame(webelement)
switch_to.frame(0) <- direct pass index its 0 if only one frame is present

driver.switch_to.default_content() <= switched back to main window
driver.switch_to.parent_frame()
if there is frame within the frame we dont need to use default_content

frame iframe form
'''
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame()

time.sleep(5)
driver.quit()