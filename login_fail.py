from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = r"C:\Users\ashis\OneDrive\Desktop\chromedriver-win32\chromedriver-win32\chromedriver.exe"

service = Service(driver_path)

# Initialize WebDriver
web = webdriver.Chrome(service=service)

try:
    web.get("https://www.bewakoof.com/login")
    
    # Wait until the login input field is present
    login = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div[2]/form/div/div/input"))
    )
    login.send_keys("1234567")

    # Wait until the submit button is clickable
    submit = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div[2]/form/button"))
    )
    submit.click()

    # Check for error message
    error_message = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[2]/p"))
    )
    print("Test failed under: Please enter a valid 10 digit mobile number")
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Wait for user input to close the browser
    input("Press Enter to close the browser...")
    web.quit()
