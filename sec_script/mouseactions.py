import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

'''

mouse hover -> move_to_element(element)
right click -> context_click(btn).perform()
double click ->  double_click(btn).perform()
drag and drop ->

'''
service = Service(executable_path="C:/Drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()


act = ActionChains(driver)
btn = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act.context_click(btn).perform()

'''
act.move_to_element(admin).move_to_element(user).click().perform()
'''

time.sleep(5)
driver.quit()