from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

location = os.getcwd()

def set_chrome():
    service = Service(executable_path="C:/Drivers/chromedriver-win64/chromedriver.exe")
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(service=service, options=ops)
    return driver

driver = set_chrome()
driver.get("https://file-examples.com/index.php/sample-documents-download/")
driver.maximize_window()
driver.implicitly_wait(10)

# Optional: Switch to iframe if the content is inside one
# iframe = driver.find_element(By.XPATH, "//iframe")
# driver.switch_to.frame(iframe)

# Wait for the download button to be visible and clickable
download_link = driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]")
download_link.click()

time.sleep(5)
driver.quit()


'''
save_screenshot(path)
driver.switch_to.new_window('tab')


'''