import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)
        homePage.getFormName().send_keys(getData["firstname"])
        homePage.getFormEmail().send_keys(getData["email"])
        homePage.getFormPass().send_keys(getData["pass"])
        homePage.getFormCheckBox().click()
        self.selectOptionByText(homePage.getFormDropDown(), getData["gender"])

        homePage.getFormRadioButton().click()
        homePage.getFormSubmitButton().click()
        message = homePage.getFormAlertMessage().text
        print(message)
        assert not "Success" in message
        self.driver.refresh()


    @pytest.fixture(
        params=[{"firstname": "Manas Ranjan", "email": "manas@gmail.com", "pass": "123456", "gender": "Male"},
                {"firstname": "Ankita S", "email": "ankita@gmail.com", "pass": "123456", "gender": "Female"}])
    def getData(self, request):
        return request.param
