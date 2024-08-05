from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver_path = r"C:\Users\ashis\OneDrive\Desktop\chromedriver-win32\chromedriver-win32\chromedriver.exe"

service = Service(driver_path)

web = webdriver.Chrome(service=service)


web.get("https://www.bewakoof.com/")
    
time.sleep(1)
    
search = web.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/header/div[2]/div/div[3]/div[2]/div/form/input")
search.send_keys("shirt")
search.send_keys(Keys.RETURN)
first = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/a"))
    )

first.click()
   

input("Press Enter to close the browser...")

web.quit()