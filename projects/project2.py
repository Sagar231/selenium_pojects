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


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame("frame-one796456169")
driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-0']").send_keys("sagar")
driver.find_element(By.XPATH,"//label[@for='RESULT_RadioButton-1_0']").click()
cal = driver.find_element(By.XPATH,"//*[@id='q4']/span").click()

mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
while True:
    if mon == "January":
        break
    else:
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Next']")))
        next_button.click()

drp = driver.find_element(By.XPATH,"//select[@aria-label='Select year']")
drpsel = Select(drp)
drpsel.select_by_value("2025")





time.sleep(5)
driver.quit()
