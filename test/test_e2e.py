from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckOutPage import CheckOut
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        homePage = HomePage(self.driver)
        results = homePage.getProductTitles()
        checkOutPage = CheckOut(self.driver)
        log.info("Getting all card titles")

        homePage.getShopPage().click()
        for result in results:

            if result.find_element(By.CSS_SELECTOR, "div div h4").text == "Blackberry":
                result.find_element(By.CSS_SELECTOR, "div div button").click()
        homePage.getGoToCheckOutPage().click()

        homePage.getSuccess().click()
        checkOutPage.getCountryName().send_keys("ind")
        countries = checkOutPage.getCountriesName()
        for country in countries:
            if country.text == "India":
                country.click()
                break
        checkOutPage.getSelectCountry().click()
        checkOutPage.getSelectButton().click()
        log.info("Text matching!!")
        print(checkOutPage.getMessage().text)
