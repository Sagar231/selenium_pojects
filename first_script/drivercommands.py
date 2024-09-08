'''
application (get) commands
conditional        //
browser            //
navigation         //
wait               //
'''

'''
application commands
get()  - opening the url
driver.title - capture the title of the page
driver.current_url - capture the url of the page
driver.page_source - source code for the page
'''

'''
conditional commands

is_displayed()
is_enabled()
is_selected()

'''

'''
browser 

close()  -  it will close a single browser window and the process might be keep running in backend (parent browser gets close)
quit()  - it will close all browser windows and kills the process 

'''

'''
navigation

back()
forward()
refresh()

'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.com")
time.sleep(10)
driver.back()
# driver.forward()
#
# driver.refresh()
time.sleep(5)
driver.quit()
# driver.back()

'''
wait



'''
