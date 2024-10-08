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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait for the username input to be visible
try:
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("Admin")

    # Wait for the password input and interact
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys("admin123")

    # Wait for the login button and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button.orangehrm-login-button"))
    )
    login_button.click()

    # Verify the login by checking the page title
    act_title = driver.title
    exp_title = "OrangeHRM"

    if act_title == exp_title:
        print("Login test passed")
    else:
        print("Login test failed")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Pause the script until you manually press Enter
    input("Press Enter to close the browser...")

    # Close the browser
    driver.quit()

'''

find_element vs find_elements

find_element() - returns single webelement
find_elements() - returns multiple 

find_element() - returns single webelement we can use send keys
find_elements() - even if there is only one element we cant use send keys cause it will return the output as list collection

find_element() - returns NoSuchElementException if element not available
find_elements() - returns empty list or nothing if no such element is there

'''


'''

text vs get_attribute('value')

text - just gives the inner text
get_attribute - gives whatever displayed or the name of the value or id or name


'''
