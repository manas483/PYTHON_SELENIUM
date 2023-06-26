from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("headless")

actualProducts = []
service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
results = driver.find_elements(By.CSS_SELECTOR, ".col-lg-3.col-md-6.mb-3")

for result in results:
    if result.find_element(By.CSS_SELECTOR, "div div h4").text == "Blackberry":
        result.find_element(By.CSS_SELECTOR, "div div button").click()
driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
driver.find_element(By.ID, "country").send_keys("ind")
countries = driver.find_elements(By.CSS_SELECTOR, ".suggestions ul li")
for country in countries:
    if country.text == "India":
        country.click()
        break
driver.find_element(By.CSS_SELECTOR, "div label").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()
print(driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text)
driver.quit()
