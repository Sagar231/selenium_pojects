'''
wait

time.sleep -> we can use but not a wait statement but the performance is poor and if it still loading it will give exception

implicit wait
    1) single statement
    2) performance will be good
    disadv - if the element within the time limit we gave it will through an error

explicit wait
   we also use condition


'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path="C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)

mywait  = WebDriverWait(driver,10)
'''
driver.implicitly_wait(10) #applicable for all the statement
'''


driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME,'q')

searchbox.send_keys("Selenium")
searchbox.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[normalize-space()='Selenium']")))
searchlink.click()

driver.quit()





