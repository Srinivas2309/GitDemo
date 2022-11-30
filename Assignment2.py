
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service(r"C:\Users\Srinivas\Downloads\chromedriver_win32 (3)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME,"blinkingText").click()
windowsopened = driver.window_handles
driver.switch_to.window(windowsopened[1])
message = driver.find_element(By.CLASS_NAME,"red").text
print(message)
var = message.split("at")[1].strip().split(" ")[0]    # Not understood confusing
print(var)
driver.close()
driver.switch_to.window(windowsopened[0])
driver.find_element(By.ID,"username").send_keys(var)
driver.find_element(By.ID,"password").send_keys(var)
driver.find_element(By.ID,"signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located(((By.CSS_SELECTOR),".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR,".alert-danger").text)
