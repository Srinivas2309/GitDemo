import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actuallist = []
service_obj= Service(r"C:\Users\Srinivas\Downloads\chromedriver_win32 (3)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)  # It will wait max of 5 seconds
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")

count = len(results)
assert count > 0
for result in results:
    actuallist.append(result.find_element(By.XPATH,"h4").text)   # chaining of web elements

    result.find_element(By.XPATH,"div/button").click()   # confusing   we called this has chaining of web elements
print(actuallist)
assert expectedlist == actuallist
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation
prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum =0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalamount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totalamount


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)     # Explicit wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo"))) # explicit wait
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
assert driver.find_element(By.CSS_SELECTOR,".promoInfo").text


amount = int(driver.find_element(By.CLASS_NAME,"totAmt").text)
discountamount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert amount > discountamount