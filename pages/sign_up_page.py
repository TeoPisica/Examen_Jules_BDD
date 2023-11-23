from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class SignUpPage(BasePage):

    FIRST_NAME_LABEL = (By.XPATH, '[//strong[text()="first name..."]/parent::span/parent::div]/parent::div//input')
    LAST_NAME_LABEL = (By.XPATH, '//strong[text()="last name..."]')
    INPUT = (By.XPATH, '//input')
    PERSONAL_OPTION = (By.XPATH, '//input[@value="personal"]')
    CONTINUE_BUTTON = (By.XPATH, '//span[text()="CONTINUE"]')
    EMAIL_ERROR = (By.XPATH, '//p[contains(text(), "address")]')


    def validate_last_name_label_is_displayed(self):
        assert self.driver.find_element(*self.LAST_NAME_LABEL).is_displayed(), 'Last name label not displayed'

    def complete_first_name_input(self, first_name):
        self.wait_for_elem(*self.FIRST_NAME_LABEL)
        self.driver.find_element(*self.FIRST_NAME_LABEL).send_keys(first_name)

    def complete_last_name_input(self, last_name):
        self.validate_last_name_label_is_displayed()
        self.driver.find_element(*self.INPUT).send_keys(last_name)

    def click_personal_option(self):
        self.wait_for_elem(*self.PERSONAL_OPTION)
        self.driver.find_element(*self.PERSONAL_OPTION).click()

    def click_continue_button(self):
        self.wait_for_elem(*self.CONTINUE_BUTTON)
        sleep(1)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def press_enter(self):
        self.wait_for_elem(*self.INPUT)
        sleep(1)
        self.driver.find_element(*self.INPUT).send_keys(Keys.ENTER)

    def complete_input(self, value):
        self.wait_for_elem(*self.INPUT)
        sleep(2)
        self.driver.find_element(*self.INPUT).send_keys(value)
        sleep(2)

    def validate_email_error(self, error_text):
        assert self.driver.find_element(*self.EMAIL_ERROR).is_displayed(), 'Error not displayed'
        assert self.driver.find_element(*self.EMAIL_ERROR).text == error_text, 'Wrong error'



