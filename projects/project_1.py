import time
from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the service for ChromeDriver
service = Service(executable_path="C:\Drivers\chromedriver-win64\chromedriver.exe")

# Start the browser session
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

searchform = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']"))
)
searchbtn = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@type='submit']"))
)
searchform.send_keys("Selenium")
searchbtn.click()

searchresult = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']//a"))
)
for link in searchresult:
    link.click()

winIDs = driver.window_handles
time.sleep(5)
for id in winIDs:
    driver.switch_to.window(id)
    print(driver.title)
    if driver.title != "Automation Testing Practice":
       driver.close()

time.sleep(3)
driver.quit()


