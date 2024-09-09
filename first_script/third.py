from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)
# demo.nopcommerce.com/
driver.get("https://www.facebook.com/")
driver.maximize_window()
# css selectors
'''
TAG IS ALWAYS OPTIONAL
tag id  tagname#valueofid
tag class  tagname.valueoftheclass
tag attribute  tagname[attribute=value]
tag class attribute  tagname.valueoftheclass[attribute=value]
'''

# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")

driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")
# Pause the script until you manually press Enter
input("Press Enter to close the browser...")

# Close the browser
driver.quit()