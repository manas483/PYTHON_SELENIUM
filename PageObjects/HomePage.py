from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "div ul li:nth-child(2)")
    products = (By.CSS_SELECTOR, ".col-lg-3.col-md-6.mb-3")
    name = (By.CSS_SELECTOR, "div div h4")
    names = (By.CSS_SELECTOR, "div div button")
    goToCheckOut = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    success = (By.CSS_SELECTOR, ".btn.btn-success")
    formName = (By.NAME, "name")
    formEmail = (By.CSS_SELECTOR, "input[name='email']")
    formPass = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    dropDown = (By.ID, "exampleFormControlSelect1")
    radioButton = (By.ID, "inlineRadio1")
    submitButton = (By.XPATH, "//input[@type='submit']")
    alertMessage = (By.CLASS_NAME, "alert-success")
    clearMessage = (By.XPATH, "(//input[@name='name'])[2]")

    def getFormName(self):
        return self.driver.find_element(*HomePage.formName)

    def getFormEmail(self):
        return self.driver.find_element(*HomePage.formEmail)

    def getFormPass(self):
        return self.driver.find_element(*HomePage.formPass)

    def getFormCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getFormDropDown(self):
        return self.driver.find_element(*HomePage.dropDown)

    def getFormRadioButton(self):
        return self.driver.find_element(*HomePage.radioButton)

    def getFormSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getFormAlertMessage(self):
        return self.driver.find_element(*HomePage.alertMessage)

    def getClearMessage(self):
        return self.driver.find_element(*HomePage.clearMessage)

    def getShopPage(self):
        return self.driver.find_element(*HomePage.shop)

    def getProductTitles(self):
        return self.driver.find_elements(*HomePage.products)

    def getProductName(self):
        return self.driver.find_element(*HomePage.name)

    def getAddToCart(self):
        return self.driver.find_element(*HomePage.names)

    def getGoToCheckOutPage(self):
        return self.driver.find_element(*HomePage.goToCheckOut)

    def getSuccess(self):
        return self.driver.find_element(*HomePage.success)
