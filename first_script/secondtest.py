
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path="C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)
# demo.nopcommerce.com/
driver.get("http://www.automationpractice.pl")

driver.maximize_window()

# Wait for the username input to be visible
try:
    # search_input = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "search_query_top"))
    # )
    # search_input.send_keys("Faded Short Sleeve T-shirts")
    # driver.find_element(By.LINK_TEXT,"Sign in").click()

    # driver.find_element(By.PARTIAL_LINK_TEXT,"Sig").click()

    sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container") #tagname works same way
    print(len(sliders))
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Pause the script until you manually press Enter
    input("Press Enter to close the browser...")

    # Close the browser
    driver.quit()