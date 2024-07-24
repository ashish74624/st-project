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

web.get("https://www.bewakoof.com/") 


time.sleep(1)


search = web.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/header/div[2]/div/div[3]/div[2]/div/form/input") 
search.send_keys("shirt")
search.send_keys(Keys.RETURN)

# Wait for the search results to load and find the first product
first_product = WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/a"))  
)
first_product.click()

# Wait for the product page to load
WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[8]/div/div[2]"))  
)

# Select the size of the cloth
size_selector = WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[7]/div[2]/div[1]/div[2]/div/div[3]/div"))  
)
size_selector.click()
size_option = WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[7]/div[2]/div[1]/div[2]/div/div[3]/div"))  
)
size_option.click()

# Click on the "Add to Cart" button
add_to_cart_button = web.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[8]/div/div[2]")  
add_to_cart_button.click()

# Click on the "Cart" button to view the cart
cart_button = WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/header/div[2]/div/div[3]/div[1]/div/span[1]/a"))  
)
cart_button.click()

input("Press Enter to close the browser...")


web.quit()