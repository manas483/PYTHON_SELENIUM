from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("MANAS RANJAN")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("sachan@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
# driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("Tiku")
driver.find_element(By.XPATH, "(//input[@name='name'])[2]").clear()
