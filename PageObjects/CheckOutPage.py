from selenium.webdriver.common.by import By


class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    countries = (By.CSS_SELECTOR, ".suggestions ul li")
    selectCountry = (By.CSS_SELECTOR, "div label")
    selectButton = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
    msg = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def getCountryName(self):
        return self.driver.find_element(*CheckOut.country)

    def getCountriesName(self):
        return self.driver.find_elements(*CheckOut.countries)

    def getSelectCountry(self):
        return self.driver.find_element(*CheckOut.selectCountry)

    def getSelectButton(self):
        return self.driver.find_element(*CheckOut.selectButton)

    def getMessage(self):
        return self.driver.find_element(*CheckOut.msg)
