import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME, "blinkingText").click()
windowsOpen = driver.window_handles
driver.switch_to.window(windowsOpen[1])
text = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text.split(" ")
totalText = text[4]
driver.switch_to.window(windowsOpen[0])
driver.find_element(By.ID, "username").send_keys(totalText)
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()
time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12").text)
driver.quit()
