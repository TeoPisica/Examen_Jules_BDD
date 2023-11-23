from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class AddPage(BasePage):
    PROPERTY = (By.XPATH, '//a[@href="/add/property"]')
    PERSON = (By.XPATH, '//a[@href="/add/person"]')
    NO_THANKS_BUTTON = (By.XPATH, '//button[contains(text(),"No Thanks")]')

    def click_property(self):
        self.driver.find_element(*self.PROPERTY).click()

    def click_person(self):
        self.driver.find_element(*self.PERSON).click()

    def click_no_thanks(self):
        self.wait_for_elem(*self.NO_THANKS_BUTTON)
        self.driver.find_element(*self.NO_THANKS_BUTTON).click()

