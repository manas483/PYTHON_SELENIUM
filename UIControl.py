from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radioButtonC in radioButtons:
    if radioButtonC.get_attribute("value") == "radio2":
        radioButtonC.click()
        print(radioButtonC.is_selected())
        assert radioButtonC.is_selected()
        break
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
checkboxes[2].click()
assert checkboxes[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
