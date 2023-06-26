import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

a = []
options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)
service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for result in results:

    if result.find_element(By.XPATH, "h4").text == "Raspberry - 1/4 Kg":
        result.find_element(By.XPATH, "div/button").click()
        # for result in results:
driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
promoText = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(promoText)
driver.find_element(By.XPATH, "//button[contains(.,'Place Order')]").click()
