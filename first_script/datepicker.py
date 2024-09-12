from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service = Service(executable_path="C:/Drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# Switch to the iframe that contains the datepicker input
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

month = "June"
year = "2025"
day = "16"

calinput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='datepicker']")))
calinput.click()

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Next']")))
        next_button.click()

# Wait for the dates to be available and select the right one
dates = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")))

for ele in dates:
    if ele.text == day:
        ele.click()
        break


x = input("enter to exit the driver..")
driver.quit()
