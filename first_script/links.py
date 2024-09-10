'''
internal
external
broken link - not working right now

'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.nopcommerce.com/")
driver.maximize_window()

try:
    # Wait for the input element to be clickable, then click it
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body//div/div/div[1]/div/label/input"))
    )
    search_box.click()
except Exception as e:
    print(f"Error: {e}")

# Quit the browser
driver.quit()

''''

broken links handle




'''
