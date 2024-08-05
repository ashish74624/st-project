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

web.get("https://www.bewakoof.com/login")

try:
    login = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/form/div/div/input"))
    )
    login.send_keys("1234567890")

    try:
        overlay = WebDriverWait(web, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "wzrk-overlay"))
        )
        web.execute_script("arguments[0].click();", overlay)
    except:
        pass  

    submit = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/form/button"))
    )
    web.execute_script("arguments[0].scrollIntoView();", submit)
    web.execute_script("arguments[0].click();", submit)

    input("Press Enter to close the browser...")

finally:
    web.quit()
