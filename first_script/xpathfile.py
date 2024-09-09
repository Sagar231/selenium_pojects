'''
xpath is defined as xml path
it is a syntax or language for finding on the web page using XML path expression
Xpath is used to find the location of any element on a webpage using HTML DOM structure
Xpath can be used to navigate through elements and attributes in DOM
Xpath is an address of the element

syntax of writing relative xpath

//tagname[@attribute = 'value']
// *[@attribute = 'value']
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)
# demo.nopcommerce.com/
driver.get("http://www.automationpractice.pl")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='search_query_top' or @name='search_query']").send_keys("T-shirt")
driver.find_element(By.XPATH,"//button[@name='submit_search']").click()

# we can use [or,and] type of operators with xpath
'''
//*[contains(@id,st)] it will check if id contains st
//*[starts-with(@id,'st')]
//a[text()="some inner text of the tag"]
'''

# Pause the script until you manually press Enter

'''
### XPATH-axes
self,parent,child,ancestor,descendant,following,following-sibling,preceding,preceding-sibling
//*[attribute='value]/child::tagname
//*[attribute='value]/parent::tagname
//*[attribute='value]/following::tagname
//*[attribute='value]/preceding::tagname
//*[attribute='value]/ancestor::tagname
//*[attribute='value]/descendant::tagname

//current html tag[attribute='value]/following-sibling::sibling tag[@attribute='value']
//current html tag[attribute='value]/preceding-sibling::previous tag[@attribute='value']
'''

input("Press Enter to close the browser...")

# Close the browser
driver.quit()