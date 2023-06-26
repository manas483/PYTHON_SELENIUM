from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

actualVegetables = []
service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# sortedVegetables = ['Almond', 'Apple', 'Banana', 'Beans', 'Brinjal']

driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()
products = driver.find_elements(By.CSS_SELECTOR, "tbody tr td:first-child")
productList = []
for product in products:
    productList.append(product.text)
sortedVegetables = productList.copy()
productList.sort()
assert productList == sortedVegetables
driver.quit()
