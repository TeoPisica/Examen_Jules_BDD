from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class ForgotPassPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    SEND_EMAIL_BUTTON = (By.XPATH, '//button[@type="button"]')
    ERROR = (By.XPATH, '//p[contains(text(), "email")]')
    ERROR_LIST = (By.XPATH, '//p[contains(text(), "email")]')

    def set_email(self, email):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def clear_email(self):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).clear()

    def validate_send_email_button_is_enabled(self):
        assert self.driver.find_element(*self.SEND_EMAIL_BUTTON).is_enabled(), 'Button is disabled'
        self.click_send_email_button()

    def click_send_email_button(self):
        self.wait_for_elem(*self.SEND_EMAIL_BUTTON)
        self.driver.find_element(*self.SEND_EMAIL_BUTTON).click()


    def validate_send_email_button_is_disabled(self):
        sleep(5)
        assert self.driver.find_element(*self.SEND_EMAIL_BUTTON).is_enabled() is not True, 'Button is enabled'

    def validate_invalid_email_error(self):
        assert self.driver.find_element(*self.ERROR).is_displayed(), 'Error not displayed'
        assert self.driver.find_element(*self.ERROR).text == 'Please enter a valid email address!', 'Wrong error'

    def validate_invalid_email_error_not_displayed(self):
        assert len(self.driver.find_elements(*self.ERROR)) == 0, 'Error is displayed'
