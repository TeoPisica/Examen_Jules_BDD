from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class AddPersonPage(BasePage):
    FIRST_NAME_INPUT = (By.XPATH, '//label[contains(text(), "First")]/parent::div//div//input')
    LAST_NAME_INPUT = (By.XPATH, '//label[contains(text(), "Last")]/parent::div//div//input')
    SAVE_BUTTON = (By.XPATH, '//span[contains(text(), "Save")]')
    SUCCES_MESSAGE = (By.XPATH, '//span[contains(., "was added successfully")]')
    FINISH_BUTTON = (By.XPATH, '//span[contains(text(), "Finish")]')

    def set_first_name(self,name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(name)

    def set_last_name(self,name):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(name)

    def click_save_button(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()
        sleep(2)

    def verify_success_message(self):
        assert self.driver.find_element(*self.SUCCES_MESSAGE).is_displayed(), 'The message is not displayed!'


    def click_finish_button(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
        sleep(3)
