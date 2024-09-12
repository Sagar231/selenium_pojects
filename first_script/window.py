import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''

current_window_handle ---> return winID of a single browser window
window_handles  ---> return win IDs of multiple browser windows

'''
service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# winid = driver.current_window_handle
# print(winid)
mylink = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT,"OrangeHRM, Inc"))
)
mylink.click()
winids = driver.window_handles

parentwin = winids[0]
childwin = winids[1]

driver.switch_to.window(childwin)
print(driver.title)
driver.switch_to.window(parentwin)
print(driver.title)

time.sleep(20)
driver.quit()