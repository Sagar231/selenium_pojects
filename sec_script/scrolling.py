from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

service = Service(executable_path="C:/Drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(10)

# driver.execute_script("window.scrollBy(0,3000)","")

#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# value=driver.execute_script("return window.pageYOffset;")
# print("Number if pixels moved:", value)

flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)

value=driver.execute_script("return window.pageYOffset;")
print("Number if pixels moved:", value)

time.sleep(5)
driver.quit()