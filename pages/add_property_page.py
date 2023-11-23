import button as button
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class AddPropertyPage(BasePage):
    PROPERTY_NICKNAME = (By.XPATH, '//input[@type="text"]')
    CONTINUE_BUTTON = (By.XPATH, '//span[contains(text(),"Continue")]')
    ADDRESS = (By.XPATH, '//label[contains(text(), "Address")]/parent::div//div//input')
    PARCEL = (By.XPATH, '//label[contains(text(), "Registered")]/parent::div//div//input')
    SAVE_PROPERTY_BUTTON = (By.XPATH, '//span[contains(text(), "Save")]')
    SUCCES_MESSAGE = (By.XPATH, '//span[contains(text(), "successfully")]')
    FINISH_BUTTON = (By.XPATH, '//span[contains(text(), "Finish")]')

    def set_property_nickname(self, name):
        self.driver.find_element(*self.PROPERTY_NICKNAME).send_keys(name)
        sleep(2)

    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        sleep(2)

    def fill_property_address(self,address):
        self.driver.find_element(*self.ADDRESS).send_keys(address)

    def fill_property_parcel(self,number):
        self.driver.find_element(*self.PARCEL).send_keys(number)

    def click_save_button(self):
        button = self.driver.find_element(*self.SAVE_PROPERTY_BUTTON)
        button.location_once_scrolled_into_view
        button.click()

    def verify_success_message(self):
        assert self.driver.find_element(*self.SUCCES_MESSAGE).is_displayed(), 'The message is not displayed!'


    def click_finish_button(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()