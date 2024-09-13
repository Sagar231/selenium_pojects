from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

'''

mouse hover -> move_to_element(element)
right click -> context_click(btn).perform()
double click ->  double_click(btn).perform()
drag and drop -> drag_and_drop(btn).

slider elements 

-> min_slider = find...
min_slider.location => {'x':59,'y':252}
max_slider.location =>{'x':639,'y':252}

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

drag_and_drop_by_offset(slider,X,Y)
'''
service = Service(executable_path="C:/Drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()


act = ActionChains(driver)
srcbtn = driver.find_element(By.ID,"box6")
targetbtn = driver.find_element(By.ID,"box106")

act.drag_and_drop(srcbtn,targetbtn).perform()



time.sleep(5)
driver.quit()